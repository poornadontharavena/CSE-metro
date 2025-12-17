import streamlit as st
import qrcode
from io import BytesIO
import uuid
from PIL import Image
from gtts import gTTS
import base64

def generate_qr(data):
    qr=qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    return img


st.title(" metro ticket booking system with qr code")
stations=("Ammerpet","miyapur","LB nagar","KPHB","JNTU")
name=st.text_input("passenger name")
source=st.selectbox("source station",stations)
destination=st.selectbox("Destination station",stations)
no_tickets=st.number_input("number of tickets",min_value=1,value=1)
price_per_ticket=30
total_amount=no_tickets * price_per_ticket
st.info(f"Total Amount:(total_amount)")

#BOOKING BUTTON

if st.button("BOOK TICKET"):
    if name.strip()=="":
        st.error("please enter the passenger name.")
    elif source==destination:
        st.error("source and destination cannot be same.")
    else:
        #generate booking ID
        booking_id=str(uuid.uuid4())[:8]
        #-----------------------
        #qr code generation
        #-----------------------
        qr_data=(
            f"BookingID:{booking_id}\n"
            f"Name:{name}\nFrom:{source}\nTo:{destination}\n tickets:{no_tickets}\n")
        qr_img=generate_qr(qr_data)
        buf=BytesIO()
        qr_img.save(buf,format="PNG")
        qr_bytes=buf.getvalue()

        st.success("ticket booked sucessfully!")

        st.write("ticket details")
        st.write(f"Booking Id:(booking_id)")
        st.write(f"passanger:(name)")
        st.write(f"from:(source)")
        st.write(f"To:(destination)")
        st.write(f"Tickets: (no_tickets)")
        st.write(f"Amount paid:rs{total_amount}")
        st.image(qr_bytes,width=250)
