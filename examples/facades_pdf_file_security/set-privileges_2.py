# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesecurity\set-privileges
# Code fence language: python


from aspose.pdf.facades import PdfFileSecurity, DocumentPrivilege

def set_privilege_with_password():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "sample.pdf"
    output_pdf = data_dir + "SamplePrivilegesPassword_out.pdf"

    # Create DocumentPrivilege object and configure permissions
    privilege = DocumentPrivilege.forbid_all
    privilege.change_allow_level = 1
    privilege.allow_print = True
    privilege.allow_copy = True

    file_security = PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(input_pdf)

    # Set privilege with passwords
    # user_password is empty, owner_password is set
    file_security.set_privilege(
        "",                 # user password
        "P@ssw0rd",         # owner password
        privilege
    )

    # Save PDF with updated privileges
    file_security.save(output_pdf)
