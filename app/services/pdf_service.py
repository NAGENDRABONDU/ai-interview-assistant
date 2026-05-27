from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    session,
    report,
    output_file
):

    doc = SimpleDocTemplate(
        output_file
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Interview Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Role: {session['role']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Experience: {session['experience']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Interview Type: {session['interview_type']}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Total Questions: {report['totalQuestions']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Total Score: {report['totalScore']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Average Score: {report['averageScore']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Performance: {report['performance']}",
            styles["Normal"]
        )
    )

    doc.build(content)

    return output_file