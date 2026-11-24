
"""Build the public English CV with ReportLab."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer


OUTPUT = Path(__file__).resolve().parents[1] / "static" / "uploads" / "Xufan-Gao-CV.pdf"
INK = colors.HexColor("#192A36")
MUTED = colors.HexColor("#425565")
ACCENT = colors.HexColor("#17615E")


STYLE = {
    "name": ParagraphStyle("Name", fontName="Helvetica-Bold", fontSize=29,
                           leading=34, textColor=INK, spaceAfter=4),
    "role": ParagraphStyle("Role", fontSize=12, leading=16, textColor=ACCENT, spaceAfter=5),
    "contact": ParagraphStyle("Contact", fontSize=9, leading=13, textColor=MUTED),
    "section": ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=13,
                              leading=17, textColor=ACCENT, spaceBefore=14, spaceAfter=5,
                              keepWithNext=True),
    "body": ParagraphStyle("Body", fontSize=10, leading=14, textColor=INK, spaceAfter=6),
}


def link(label, url):
    return f'<link href="{url}" color="#17615E"><u>{label}</u></link>'


def draw_footer(canvas, document):
    width, _ = A4
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#CED9DD"))
    canvas.line(document.leftMargin, 16 * mm, width - document.rightMargin, 16 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(document.leftMargin, 11 * mm, "Xufan Gao  /  Academic CV")
    canvas.drawRightString(width - document.rightMargin, 11 * mm, str(document.page))
    canvas.restoreState()


def build():
    document = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4, title="Xufan Gao | Academic CV", author="Xufan Gao",
        leftMargin=21 * mm, rightMargin=21 * mm, topMargin=18 * mm, bottomMargin=23 * mm,
    )
    email = link("gxf1212@zju.edu.cn", "mailto:gxf1212@zju.edu.cn")
    github = link("GitHub", "https://github.com/gxf1212")
    scholar = link("Google Scholar", "https://scholar.google.com/citations?user=f8pi1BUAAAAJ")
    orcid = link("ORCID", "https://orcid.org/0009-0004-0065-3172")
    portfolio = link("Academic portfolio", "https://gxf1212.github.io/academic-cv/")

    story = [
        Paragraph("Xufan Gao", STYLE["name"]),
        Paragraph("Doctoral Researcher in Computational Biophysics", STYLE["role"]),
        Paragraph("Zhejiang University | Hangzhou, China", STYLE["contact"]),
        Paragraph(" &nbsp;|&nbsp; ".join([email, github, scholar, orcid, portfolio]), STYLE["contact"]),
        Spacer(1, 3 * mm),
    ]

    def section(title, entries):
        story.append(Paragraph(title, STYLE["section"]))
        story.extend(Paragraph(entry, STYLE["body"]) for entry in entries)

    section("Research Profile", [
        "I study molecular recognition and assembly using molecular dynamics, free-energy methods, "
        "and machine learning. I develop reproducible workflows for drug discovery and biomaterials research.",
    ])

    section("Education", [
        "<b>Zhejiang University</b> | Doctoral studies in Biophysics, 2022-present<br/>"
        "Advisor: Prof. Ruhong Zhou.",
        "<b>Xi'an Jiaotong University</b> | B.Sc. in Biotechnology, 2018-2022<br/>"
        "Honor Science Program (Zhufeng Project).",
        "<b>National University of Singapore</b> | Exchange study and undergraduate research, Jan-May 2021.",
        "<b>University of Alberta</b> | Summer Enrichment Program in Applied Mathematics, Jul-Aug 2019.",
    ])

    section("Peer-Reviewed Publications", [
        "Shi, Z.*, <b>Gao, X.*</b>, Buratto, D., &amp; Zhou, R. (2025). SAGE: A Segment-Anchor-Guided "
        "Exploration Framework for the Optimization of CDK7 Inhibitors as Promising Cancer Therapy. "
        "<i>Journal of Physical Chemistry B</i>, 129(34), 8641-8651. "
        + link("DOI", "https://doi.org/10.1021/acs.jpcb.5c02076")
        + "<br/>* Equal contribution.",
        "Wang, Y., Hu, J., <b>Gao, X.</b>, et al. (2024). cAMP-independent DNA binding of the CRP family "
        "protein DdrI from <i>Deinococcus radiodurans</i>. <i>mBio</i>, 15(7), e01144-24. "
        + link("DOI", "https://doi.org/10.1128/mbio.01144-24"),
    ])

    section("Selected Preprints", [
        "Shi, Z., Zheng, X., <b>Gao, X.</b>, et al. (2026). ETALON: Verified Execution and Persistent "
        "Research Memory for Agentic Computer-Aided Drug Design. <i>ChemRxiv</i>. "
        + link("DOI", "https://doi.org/10.26434/chemrxiv.15011490/v1"),
        "Wang, P., Shi, Z., <b>Gao, X.</b>, &amp; Zhou, R. (2026). MolJam: A Multidimensional Framework "
        "for Assessing Molecular Dataset Quality and Its Impact on Machine Learning. <i>bioRxiv</i>. "
        + link("DOI", "https://doi.org/10.64898/2026.08.21.746384"),
        "Zhou, R., Zhang, G., Fu, Y., Buratto, D., Chan, K., Wang, H., Huang, Y., Gong, S.-M., "
        "Xu, C., <b>Gao, X.</b>, Huang, L., &amp; Yang, Z. (2026). Self-guided reinforcement learning "
        "enables HLA-presented peptide vaccine candidate design. <i>Research Square</i>. "
        + link("DOI", "https://doi.org/10.21203/rs.3.rs-9120093/v1"),
    ])

    story.append(PageBreak())

    section("Research Experience", [
        "<b>Graduate Researcher | Zhejiang University, 2022-present</b><br/>"
        "Develop molecular simulation and free-energy workflows for biomolecular interactions and drug design. "
        "Combine coarse-grained simulation and interpretable machine learning to study polymer assembly, "
        "membrane affinity, and cellular uptake.",
        "<b>Undergraduate Researcher | Xi'an Jiaotong University, 2020-2021</b><br/>"
        "Worked on virtual screening, molecular dynamics, and machine-learning models for biological and chemical datasets.",
    ])

    section("Selected Scientific Software", [
        f"<b>MolBlender</b> | {link('Documentation', 'https://molblender-docs.readthedocs.io/en/latest/')}<br/>"
        "Designed and developed a Python API and command-line toolkit that unifies molecular featurization "
        "and model screening across multiple backends.",
        f"<b>FEbuilder</b> | {link('Archived poster', 'https://doi.org/10.5281/zenodo.14059079')}<br/>"
        "Developed a tool for constructing hybrid topologies and preparing NAMD/CHARMM simulation inputs "
        "for small-molecule free-energy perturbation.",
        f"<b>PRISM</b> | {link('GitHub', 'https://github.com/AIB001/PRISM')}<br/>"
        "Contributed to free-energy perturbation workflows and documentation for a Python/GROMACS framework "
        "that automates protein-ligand simulation setup and analysis.",
    ])

    section("Presentation and Intellectual Property", [
        "<b>ACS Fall 2024</b> | Presented the FEbuilder poster (Board 107). "
        + link("Program entry", "https://acs.digitellinc.com/p/s/febuilder-a-comprehensive-webserver-to-streamline-fep-simulation-setup-in-drug-discovery-poster-board-107-601529"),
        "<b>Software copyright registration</b> | Physics- and Knowledge-Driven Tumor Neoantigen Design "
        "Platform (V1.0), China, No. 2025SR1378910 (2025).",
        "<b>Patent application</b> | Membrane affinity prediction for zwitterionic polymer monomers, "
        "China, No. 202610463008.4 (2026). Applicant: Zhejiang University.",
    ])

    section("Technical Skills", [
        "<b>Methods</b> | All-atom and coarse-grained MD, enhanced sampling, FEP, umbrella sampling, "
        "docking, virtual screening, and QSAR.",
        "<b>Tools and programming</b> | GROMACS, NAMD, AMBER, MDAnalysis, RDKit, Python, scikit-learn, "
        "XGBoost, Bash, Git, and Linux/Slurm.",
        "<b>Languages</b> | Mandarin Chinese and English.",
    ])

    section("Entrepreneurship and Service", [
        "<b>Huizhe Project</b> | Co-founded Huxi Huijing Technology Co., Ltd. and co-developed a research "
        "collaboration platform. The team won first prize at Zhejiang University's Zhiyun Cup (2024).",
        "<b>Academic service</b> | Helped develop and maintain the Institute of Quantitative Biology website. "
        "Edited articles for the College of Life Sciences' New Media Center (2022-2025).",
    ])

    document.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)


if __name__ == "__main__":
    build()
