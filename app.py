import streamlit as st
import qrcode
from io import BytesIO

def main():
    st.title("QR Code Generator")

    # Color picker for QR code fill color
    fill_color = st.color_picker("Pick a color for the QR code fill:", "#000000")

    # Color picker for QR code background color
    back_color = st.color_picker("Pick a color for the QR code background:", "#FFFFFF")

    input_data = st.text_input("Enter the data to generate the QR code:")

    if st.button("Generate QR Code"):
        if input_data:
            qr_code = generate_qr_code(input_data, fill_color, back_color)
            st.image(qr_code, use_column_width=True)

            st.markdown("### Download QR Code")
            st.download_button(
                label="Download QR Code",
                data=qr_code,
                file_name='qr_code.png',
                mime='image/png'
            )
        else:
            st.warning("Please enter data to generate the QR code.")

def generate_qr_code(data, fill_color, back_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image object with the specified fill and background colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    return img_bytes.getvalue()

if __name__ == "__main__":
    main()
