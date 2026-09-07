import streamlit as st
import pandas as pd
from datetime import datetime, date
from pathlib import Path

st.set_page_config(
    page_title="Marine Operation Vessel",
    page_icon="⚓",
    layout="wide",
)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def load_csv(name, columns):
    p = DATA_DIR / name
    if p.exists():
        return pd.read_csv(p)
    return pd.DataFrame(columns=columns)

def save_csv(df, name):
    df.to_csv(DATA_DIR / name, index=False)

# ---------- Sidebar ----------
st.sidebar.title("⚓ Marine Operation Vessel")
st.sidebar.caption("Vessel Operations Management System")

menu = st.sidebar.radio(
    "MENU",
    [
        "Dashboard",
        "Vessel Master",
        "Daily Operation",
        "Crew",
        "Fuel & Consumption",
        "Maintenance",
        "Incident / Near Miss",
        "Reports",
    ],
)

# ---------- Data ----------
vessel_cols = [
    "Vessel Name","IMO / Reg No","Vessel Type","Flag",
    "Call Sign","DWT (ton)","LOA (m)","Engine (kW)",
    "Status","Last Update"
]
op_cols = [
    "Date","Vessel","Location","Operation",
    "Activity","Start Time","End Time","Weather",
    "Wind (kn)","Wave (m)","Status","Remarks"
]
crew_cols = [
    "Name","Position","Nationality","Certificate",
    "Certificate Expiry","Medical Expiry","Status"
]
fuel_cols = [
    "Date","Vessel","Fuel Type","Opening (L)",
    "Received (L)","Consumed (L)","Closing (L)","Engine Hour"
]
maint_cols = [
    "Date","Vessel","Equipment","Maintenance Type",
    "Description","Priority","Status","Next Due"
]
incident_cols = [
    "Date","Vessel","Location","Type","Severity",
    "Description","Immediate Action","Status"
]

vessels = load_csv("vessels.csv", vessel_cols)
operations = load_csv("daily_operations.csv", op_cols)
crew = load_csv("crew.csv", crew_cols)
fuel = load_csv("fuel.csv", fuel_cols)
maintenance = load_csv("maintenance.csv", maint_cols)
incidents = load_csv("incidents.csv", incident_cols)

# ---------- Dashboard ----------
if menu == "Dashboard":
    st.title("⚓ Marine Operation Vessel")
    st.subheader("Operational Dashboard")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Vessel", len(vessels))
    c2.metric("Operation Log", len(operations))
    c3.metric("Maintenance Open", int((maintenance["Status"] == "Open").sum()) if len(maintenance) else 0)
    c4.metric("Incident Open", int((incidents["Status"] == "Open").sum()) if len(incidents) else 0)

    st.divider()

    left, right = st.columns(2)
    with left:
        st.markdown("### Vessel Status")
        if len(vessels):
            st.bar_chart(vessels["Status"].value_counts())
        else:
            st.info("Belum ada data vessel. Tambahkan melalui menu Vessel Master.")

    with right:
        st.markdown("### Operation Status")
        if len(operations):
            st.bar_chart(operations["Status"].value_counts())
        else:
            st.info("Belum ada daily operation.")

    st.markdown("### Recent Operations")
    st.dataframe(operations.tail(10), use_container_width=True, hide_index=True)

# ---------- Vessel Master ----------
elif menu == "Vessel Master":
    st.title("🚢 Vessel Master")
    with st.form("vessel_form", clear_on_submit=True):
        cols = st.columns(3)
        name = cols[0].text_input("Vessel Name *")
        imo = cols[1].text_input("IMO / Registration No")
        vtype = cols[2].selectbox("Vessel Type", ["AHTS","Tug Boat","Supply Vessel","Crew Boat","Barge","Utility Vessel","Other"])
        flag = cols[0].text_input("Flag", "Indonesia")
        call = cols[1].text_input("Call Sign")
        dwt = cols[2].number_input("DWT (ton)", min_value=0.0)
        loa = cols[0].number_input("LOA (m)", min_value=0.0)
        engine = cols[1].number_input("Engine Power (kW)", min_value=0.0)
        status = cols[2].selectbox("Status", ["Operational","Standby","Under Maintenance","Off Hire"])
        submitted = st.form_submit_button("💾 Save Vessel")

        if submitted:
            if not name:
                st.error("Vessel Name wajib diisi.")
            else:
                new = pd.DataFrame([{
                    "Vessel Name": name, "IMO / Reg No": imo, "Vessel Type": vtype,
                    "Flag": flag, "Call Sign": call, "DWT (ton)": dwt, "LOA (m)": loa,
                    "Engine (kW)": engine, "Status": status,
                    "Last Update": datetime.now().strftime("%Y-%m-%d %H:%M")
                }])
                vessels = pd.concat([vessels, new], ignore_index=True)
                save_csv(vessels, "vessels.csv")
                st.success("Data vessel berhasil disimpan.")

    st.dataframe(vessels, use_container_width=True, hide_index=True)

# ---------- Daily Operation ----------
elif menu == "Daily Operation":
    st.title("🧭 Daily Marine Operation")
    vessel_options = vessels["Vessel Name"].dropna().tolist() if len(vessels) else ["Belum ada vessel"]

    with st.form("operation_form", clear_on_submit=True):
        c = st.columns(3)
        op_date = c[0].date_input("Date", date.today())
        vessel = c[1].selectbox("Vessel", vessel_options)
        location = c[2].text_input("Location / Field")
        operation = c[0].selectbox("Operation Type", [
            "Standby","Supply Run","Towing","Anchor Handling",
            "Crew Transfer","Bunkering","Cargo Operation","Other"
        ])
        activity = c[1].text_input("Activity / Job Description")
        weather = c[2].selectbox("Weather", ["Good","Moderate","Poor","Storm"])
        start = c[0].text_input("Start Time", "08:00")
        end = c[1].text_input("End Time", "17:00")
        wind = c[2].number_input("Wind (kn)", min_value=0.0)
        wave = c[0].number_input("Wave Height (m)", min_value=0.0)
        status = c[1].selectbox("Status", ["Planned","On Going","Completed","Cancelled"])
        remarks = c[2].text_input("Remarks")
        submitted = st.form_submit_button("💾 Save Operation")

        if submitted:
            new = pd.DataFrame([{
                "Date": op_date, "Vessel": vessel, "Location": location,
                "Operation": operation, "Activity": activity,
                "Start Time": start, "End Time": end, "Weather": weather,
                "Wind (kn)": wind, "Wave (m)": wave, "Status": status, "Remarks": remarks
            }])
            operations = pd.concat([operations, new], ignore_index=True)
            save_csv(operations, "daily_operations.csv")
            st.success("Daily operation berhasil disimpan.")

    st.dataframe(operations, use_container_width=True, hide_index=True)

# ---------- Crew ----------
elif menu == "Crew":
    st.title("👷 Crew Management")
    with st.form("crew_form", clear_on_submit=True):
        c = st.columns(3)
        name = c[0].text_input("Crew Name *")
        position = c[1].selectbox("Position", ["Master","Chief Officer","2nd Officer","Chief Engineer","2nd Engineer","AB","Oiler","Bosun","Cook","Other"])
        nationality = c[2].text_input("Nationality", "Indonesia")
        cert = c[0].text_input("Main Certificate")
        cert_exp = c[1].date_input("Certificate Expiry", date.today())
        med_exp = c[2].date_input("Medical Expiry", date.today())
        status = c[0].selectbox("Status", ["On Board","Available","On Leave","Off"])
        submitted = st.form_submit_button("💾 Save Crew")
        if submitted:
            if not name:
                st.error("Crew Name wajib diisi.")
            else:
                new = pd.DataFrame([{
                    "Name": name, "Position": position, "Nationality": nationality,
                    "Certificate": cert, "Certificate Expiry": cert_exp,
                    "Medical Expiry": med_exp, "Status": status
                }])
                crew = pd.concat([crew, new], ignore_index=True)
                save_csv(crew, "crew.csv")
                st.success("Data crew berhasil disimpan.")
    st.dataframe(crew, use_container_width=True, hide_index=True)

# ---------- Fuel ----------
elif menu == "Fuel & Consumption":
    st.title("⛽ Fuel & Consumption")
    vessel_options = vessels["Vessel Name"].dropna().tolist() if len(vessels) else ["Belum ada vessel"]
    with st.form("fuel_form", clear_on_submit=True):
        c = st.columns(4)
        d = c[0].date_input("Date", date.today())
        vessel = c[1].selectbox("Vessel", vessel_options)
        ftype = c[2].selectbox("Fuel Type", ["MGO","HFO","Diesel","Lubricant"])
        opening = c[3].number_input("Opening (L)", min_value=0.0)
        received = c[0].number_input("Received (L)", min_value=0.0)
        consumed = c[1].number_input("Consumed (L)", min_value=0.0)
        engine_hr = c[2].number_input("Engine Hour", min_value=0.0)
        closing = opening + received - consumed
        c[3].metric("Calculated Closing (L)", f"{closing:,.0f}")
        submitted = st.form_submit_button("💾 Save Fuel Record")
        if submitted:
            new = pd.DataFrame([{
                "Date": d, "Vessel": vessel, "Fuel Type": ftype,
                "Opening (L)": opening, "Received (L)": received,
                "Consumed (L)": consumed, "Closing (L)": closing,
                "Engine Hour": engine_hr
            }])
            fuel = pd.concat([fuel, new], ignore_index=True)
            save_csv(fuel, "fuel.csv")
            st.success("Fuel record berhasil disimpan.")
    st.dataframe(fuel, use_container_width=True, hide_index=True)

# ---------- Maintenance ----------
elif menu == "Maintenance":
    st.title("🔧 Maintenance Management")
    vessel_options = vessels["Vessel Name"].dropna().tolist() if len(vessels) else ["Belum ada vessel"]
    with st.form("maintenance_form", clear_on_submit=True):
        c = st.columns(4)
        d = c[0].date_input("Date", date.today())
        vessel = c[1].selectbox("Vessel", vessel_options)
        equipment = c[2].text_input("Equipment")
        mtype = c[3].selectbox("Maintenance Type", ["Preventive","Corrective","Inspection","Calibration"])
        desc = c[0].text_input("Description")
        priority = c[1].selectbox("Priority", ["Low","Medium","High","Critical"])
        status = c[2].selectbox("Status", ["Open","In Progress","Completed"])
        next_due = c[3].date_input("Next Due", date.today())
        submitted = st.form_submit_button("💾 Save Maintenance")
        if submitted:
            new = pd.DataFrame([{
                "Date": d, "Vessel": vessel, "Equipment": equipment,
                "Maintenance Type": mtype, "Description": desc,
                "Priority": priority, "Status": status, "Next Due": next_due
            }])
            maintenance = pd.concat([maintenance, new], ignore_index=True)
            save_csv(maintenance, "maintenance.csv")
            st.success("Maintenance berhasil disimpan.")
    st.dataframe(maintenance, use_container_width=True, hide_index=True)

# ---------- Incident ----------
elif menu == "Incident / Near Miss":
    st.title("⚠️ Incident / Near Miss")
    vessel_options = vessels["Vessel Name"].dropna().tolist() if len(vessels) else ["Belum ada vessel"]
    with st.form("incident_form", clear_on_submit=True):
        c = st.columns(3)
        d = c[0].date_input("Date", date.today())
        vessel = c[1].selectbox("Vessel", vessel_options)
        location = c[2].text_input("Location")
        itype = c[0].selectbox("Type", ["Incident","Near Miss","Unsafe Act","Unsafe Condition","Environmental"])
        severity = c[1].selectbox("Severity", ["Low","Medium","High","Critical"])
        desc = c[2].text_area("Description")
        action = c[0].text_area("Immediate Action")
        status = c[1].selectbox("Status", ["Open","Investigation","Closed"])
        submitted = st.form_submit_button("💾 Save Report")
        if submitted:
            new = pd.DataFrame([{
                "Date": d, "Vessel": vessel, "Location": location, "Type": itype,
                "Severity": severity, "Description": desc,
                "Immediate Action": action, "Status": status
            }])
            incidents = pd.concat([incidents, new], ignore_index=True)
            save_csv(incidents, "incidents.csv")
            st.success("Incident/Near Miss berhasil disimpan.")
    st.dataframe(incidents, use_container_width=True, hide_index=True)

# ---------- Reports ----------
elif menu == "Reports":
    st.title("📊 Reports & Export")
    datasets = {
        "Vessel Master": vessels,
        "Daily Operation": operations,
        "Crew": crew,
        "Fuel": fuel,
        "Maintenance": maintenance,
        "Incident": incidents,
    }
    selected = st.selectbox("Select Report", list(datasets.keys()))
    df = datasets[selected]
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.download_button(
        "⬇️ Download CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=selected.lower().replace(" ","_") + ".csv",
        mime="text/csv",
    )

st.sidebar.divider()
st.sidebar.caption("Marine Operation Vessel • Local data storage")
