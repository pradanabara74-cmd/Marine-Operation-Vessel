import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# FLATTFORM MARITIME AI COMPANY
# 25 AI EMPLOYEES
# ============================================================

st.set_page_config(
    page_title="FLATTFORM Maritime AI",
    page_icon="⚓",
    layout="wide"
)

# ============================================================
# 25 AI EMPLOYEES
# ============================================================

AI_EMPLOYEES = [

    {
        "name": "AI CEO",
        "department": "Executive",
        "icon": "👔",
        "scope": "Strategi perusahaan, prioritas bisnis, koordinasi seluruh departemen."
    },

    {
        "name": "AI Marine Superintendent",
        "department": "Marine Operations",
        "icon": "⚓",
        "scope": "Operasi kapal, keselamatan, kesiapan kapal dan dukungan kepada Master."
    },

    {
        "name": "AI DPA",
        "department": "ISM / Safety",
        "icon": "🛡️",
        "scope": "ISM Code, SMS, safety management, audit, NCR dan corrective action."
    },

    {
        "name": "AI QHSE Manager",
        "department": "QHSE",
        "icon": "🏭",
        "scope": "Quality, Health, Safety, Environment, audit dan continuous improvement."
    },

    {
        "name": "AI Technical Superintendent",
        "department": "Technical",
        "icon": "⚙️",
        "scope": "Machinery, maintenance, dry dock, reliability dan technical defects."
    },

    {
        "name": "AI Crewing Manager",
        "department": "Crewing",
        "icon": "👨‍✈️",
        "scope": "Crew planning, certification, manning, crew welfare dan dokumentasi."
    },

    {
        "name": "AI Chief Engineer",
        "department": "Engineering",
        "icon": "🔧",
        "scope": "Engine room, machinery, maintenance dan troubleshooting."
    },

    {
        "name": "AI Master Mariner",
        "department": "Ship Operations",
        "icon": "🚢",
        "scope": "Perspektif Master, voyage execution, keselamatan dan operational decision."
    },

    {
        "name": "AI Navigation Officer",
        "department": "Navigation",
        "icon": "🧭",
        "scope": "Passage planning, bridge procedures, navigation risk dan publications."
    },

    {
        "name": "AI Cargo Specialist",
        "department": "Cargo",
        "icon": "📦",
        "scope": "Cargo planning, cargo care, loading, discharging dan cargo documentation."
    },

    {
        "name": "AI Port Operations",
        "department": "Port",
        "icon": "⚓",
        "scope": "Port call, berth planning, agent, turnaround dan port documentation."
    },

    {
        "name": "AI Chartering Manager",
        "department": "Chartering",
        "icon": "📑",
        "scope": "Charter party, fixture, laytime dan commercial-operational interface."
    },

    {
        "name": "AI Commercial Manager",
        "department": "Commercial",
        "icon": "💼",
        "scope": "Customer requirements, voyage economics dan commercial performance."
    },

    {
        "name": "AI Marine Claims",
        "department": "Claims",
        "icon": "📋",
        "scope": "Marine incident, claims, evidence, timeline dan claims preparation."
    },

    {
        "name": "AI Maritime Lawyer",
        "department": "Legal",
        "icon": "⚖️",
        "scope": "Maritime contracts, disputes, regulatory issue spotting dan legal support."
    },

    {
        "name": "AI ISPS Security Officer",
        "department": "Security",
        "icon": "🔐",
        "scope": "ISPS Code, Ship Security Plan dan maritime security."
    },

    {
        "name": "AI Environmental Officer",
        "department": "Environment",
        "icon": "🌊",
        "scope": "MARPOL, pollution prevention, waste, emissions dan environmental compliance."
    },

    {
        "name": "AI Vetting Officer",
        "department": "Vetting",
        "icon": "🔎",
        "scope": "Vetting preparation, inspection readiness dan risk gap analysis."
    },

    {
        "name": "AI SIRE Inspector",
        "department": "Inspection",
        "icon": "📝",
        "scope": "SIRE inspection preparation, observations, evidence dan close-out."
    },

    {
        "name": "AI PSC Advisor",
        "department": "Port State Control",
        "icon": "🚨",
        "scope": "PSC preparation, deficiency prevention dan corrective action."
    },

    {
        "name": "AI Procurement Manager",
        "department": "Procurement",
        "icon": "🛒",
        "scope": "Purchasing, vendor evaluation, critical spare parts dan procurement."
    },

    {
        "name": "AI Finance Manager",
        "department": "Finance",
        "icon": "💰",
        "scope": "Budget, voyage cost, financial reporting dan financial control."
    },

    {
        "name": "AI HR Manager",
        "department": "Human Resources",
        "icon": "👥",
        "scope": "HR policy, workforce planning, performance dan organization."
    },

    {
        "name": "AI Training Manager",
        "department": "Training",
        "icon": "🎓",
        "scope": "Training matrix, competency, drill, familiarization dan development."
    },

    {
        "name": "AI Maritime Intelligence",
        "department": "Intelligence",
        "icon": "🧠",
        "scope": "Maritime intelligence, trends, risks, market signals dan management briefing."
    }
]


# ============================================================
# HEADER
# ============================================================

st.title("⚓ FLATTFORM")
st.subheader("Maritime Artificial Intelligence Company")

st.write(
    "Platform AI dengan 25 AI Employees khusus industri pelayaran."
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("⚓ FLATTFORM")

st.sidebar.write("### 25 AI Employees")

departments = sorted(
    list(set(employee["department"] for employee in AI_EMPLOYEES))
)

department_filter = st.sidebar.selectbox(
    "Pilih Department",
    ["ALL"] + departments
)

if department_filter == "ALL":

    employees = AI_EMPLOYEES

else:

    employees = [
        employee
        for employee in AI_EMPLOYEES
        if employee["department"] == department_filter
    ]


employee_names = [
    employee["name"]
    for employee in employees
]

selected_name = st.sidebar.selectbox(
    "Pilih AI Employee",
    employee_names
)


selected_employee = next(
    employee
    for employee in employees
    if employee["name"] == selected_name
)


# ============================================================
# EMPLOYEE INFORMATION
# ============================================================

st.header(
    f"{selected_employee['icon']} {selected_employee['name']}"
)

st.write(
    f"**Department:** {selected_employee['department']}"
)

st.write(
    f"**Tugas:** {selected_employee['scope']}"
)

st.divider()


# ============================================================
# AI CHAT
# ============================================================

st.subheader("💬 Konsultasi dengan AI Employee")

question = st.text_area(
    "Masukkan pertanyaan atau tugas:",
    placeholder=(
        "Contoh:\n"
        "Buatkan checklist persiapan PSC kapal sebelum arrival.\n\n"
        "Atau:\n"
        "Analisa risiko operasi bunkering."
    ),
    height=180
)


# ============================================================
# AI ENGINE
# ============================================================

def local_response(employee, question):

    return f"""
### {employee['icon']} {employee['name']}

**Department:** {employee['department']}

### Analisis Awal

Pertanyaan:

> {question}

### Ruang Lingkup

Saya bertindak sebagai:

**{employee['name']}**

dengan fungsi:

{employee['scope']}

### Pendekatan

1. Identifikasi masalah utama.
2. Identifikasi kapal dan aktivitas terkait.
3. Identifikasi risiko keselamatan.
4. Identifikasi risiko operasional.
5. Identifikasi aspek compliance.
6. Periksa SMS dan prosedur perusahaan.
7. Tentukan tindakan segera.
8. Tentukan corrective action.
9. Tentukan PIC.
10. Tentukan deadline dan evidence yang diperlukan.

### Rekomendasi

Untuk keputusan yang berkaitan dengan keselamatan kapal, hukum,
sertifikasi atau compliance, keputusan akhir harus diverifikasi
terhadap prosedur perusahaan, regulasi yang berlaku dan competent person.

**FLATTFORM adalah decision-support system dan bukan pengganti Master,
DPA, Superintendent, Class, Flag State, Port Authority atau Legal Counsel.**
"""


def ai_response(employee, question):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:

        return local_response(
            employee,
            question
        )

    try:

        from openai import OpenAI

        client = OpenAI(
            api_key=api_key
        )

        prompt = f"""
You are {employee['name']}.

Department:
{employee['department']}

Professional scope:
{employee['scope']}

You are part of FLATTFORM,
an AI company for the maritime industry.

Answer professionally and practically.

Separate:
- Facts
- Assumptions
- Risks
- Recommendations
- Immediate actions
- Corrective actions
- Evidence required

Never invent maritime regulations.

For legal, safety or compliance matters,
recommend verification against current official
requirements and company SMS.

User question:

{question}
"""

        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        return response.output_text

    except Exception as error:

        return (
            local_response(
                employee,
                question
            )
            +
            f"\n\nAI connection note: {error}"
        )


# ============================================================
# ASK BUTTON
# ============================================================

if st.button(
    "🚀 ASK FLATTFORM AI",
    type="primary",
    use_container_width=True
):

    if question.strip():

        with st.spinner(
            f"{selected_employee['name']} sedang menganalisis..."
        ):

            answer = ai_response(
                selected_employee,
                question
            )

        st.markdown(answer)

    else:

        st.warning(
            "Silakan masukkan pertanyaan terlebih dahulu."
        )


# ============================================================
# DASHBOARD
# ============================================================

st.divider()

st.subheader("📊 FLATTFORM Company Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "AI Employees",
    "25"
)

col2.metric(
    "Departments",
    str(len(departments))
)

col3.metric(
    "Maritime Focus",
    "100%"
)

col4.metric(
    "Platform",
    "AI"
)


# ============================================================
# AI EMPLOYEE LIST
# ============================================================

st.divider()

st.subheader("👥 25 AI Employees")

for employee in AI_EMPLOYEES:

    with st.expander(
        f"{employee['icon']} {employee['name']} — {employee['department']}"
    ):

        st.write(
            employee["scope"]
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "FLATTFORM Maritime AI — Maritime Decision Support Platform"
)

st.caption(
    "AI output must be verified against current regulations, "
    "company SMS and competent professional judgement."
)
