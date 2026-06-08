import os
import io  # <-- Crucial for dynamic in-memory generation
from flask import Flask, render_template, request, url_for, send_file
from predict import predict_image
from report import generate_report

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ================= HOME =================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")

        if not file or file.filename == "":
            return render_template("index.html")

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        prediction, prob, intensity, contrast, edge_density = predict_image(filepath)
        image_url = url_for('static', filename='uploads/' + file.filename)

        return render_template(
            "index.html",
            image_path=image_url,
            filename=file.filename,
            prediction=prediction,
            prob=round(prob * 100, 2),
            intensity=round(intensity / 255, 4),
            contrast=round(contrast, 4),
            edge_density=round(edge_density, 4)
        )

    return render_template("index.html")


# ================= DYNAMIC REPORT GENERATION =================
@app.route("/report", methods=["POST"])
def report():
    filename = request.form.get("filename")

    if not filename:
        return "Missing filename", 400

    image_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(image_path):
        return "Image not found", 404

    # 1. Fetch fresh values dynamically
    prediction, prob, intensity, contrast, edge_density = predict_image(image_path)

    # 2. Setup in-memory stream buffer
    pdf_buffer = io.BytesIO()

    # 3. Generate the PDF layout straight into the stream
    generate_report(
        image_path,
        prediction,
        round(prob * 100, 2),
        round(intensity / 255, 4),
        round(contrast, 4),
        round(edge_density, 4),
        pdf_buffer
    )

    # 4. Rewind stream to the beginning
    pdf_buffer.seek(0)

    clean_name = os.path.splitext(filename)[0]
    download_filename = f"Stroke_Report_{clean_name}.pdf"

    # 5. Instantly trigger browser download
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=download_filename,
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)