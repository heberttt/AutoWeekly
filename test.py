from bs4 import BeautifulSoup

# Sample HTML string
html_string = "<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"><style type=\"text/css\" style=\"display:none\"><!--p{margin-top:0;margin-bottom:0}--></style></head><body dir=\"ltr\"><span style=\"font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0); background-color:rgb(255,255,255); line-height:1.5\">Dear All,</span> <div style=\"background-color:rgb(255,255,255); margin:0px\"><div style=\"direction:ltr; text-align:left; text-indent:0px; line-height:1.5; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\"><br></div><div class=\"elementToProof\" style=\"direction:ltr; text-align:left; text-indent:0px; line-height:1.5; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\">The following are the details of the (26-03-2024)&nbsp;GM<span style=\"background-color:rgb(255,255,255)\">&nbsp;</span>Location<span style=\"background-color:rgb(255,255,255)\">.</span></div><div style=\"direction:ltr; text-align:left; text-indent:0px; line-height:1.5; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\"><br></div><div class=\"elementToProof\" style=\"direction:ltr; text-align:left; text-indent:0px; line-height:1.5; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; color:rgb(0,0,0)\"><span style=\"font-size:12pt\">Date: 26</span><span style=\"font-size:16px; background-color:rgb(255,255,255)\">-03-2024</span></div><div style=\"direction:ltr; text-align:left; text-indent:0px; line-height:1.5; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt\"><span style=\"color:rgb(0,0,0)\">Time: </span><span style=\"color:currentcolor\">6:00 pm</span><span style=\"color:rgb(0,0,0)\">&nbsp;</span></div><div class=\"elementToProof\" style=\"direction:ltr; text-align:left; text-indent:0px; line-height:1.5; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\">Location: B-05-01<br>Attire: Formal&nbsp;</div><div style=\"direction:ltr; text-align:left; text-indent:0px; line-height:1.5; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\"><br></div><div style=\"direction:ltr; text-align:left; text-indent:0px; line-height:1.5; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\">Kindly be punctual and ensure you are seated at the location before GM begins.&nbsp;Latecomers will not be allowed into the room.</div></div><div style=\"text-align:left; text-indent:0px; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\"><br></div><div style=\"background-color:rgb(255,255,255); margin:0px\"><div style=\"background-color:rgb(255,255,255); margin:0px\"><div style=\"background-color:rgb(255,255,255); margin:0px\"><div style=\"background-color:rgb(255,255,255); margin:0px\"><p style=\"direction:ltr; text-align:left; line-height:1.5; background-color:white; margin:0px\"><span style=\"font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\">Thank you.</span></p></div></div></div></div><div class=\"elementToProof\" style=\"text-align:left; text-indent:0px; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\"><br>Regards.</div><div class=\"elementToProof\" style=\"text-align:left; text-indent:0px; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\">Wesley Andrew Muchilwa,<br>APD4F2311ME,</div><div class=\"elementToProof\" style=\"text-align:left; text-indent:0px; background-color:rgb(255,255,255); margin:0px; font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\">0133183420,<br>Technical Assistant.</div><div style=\"font-family:Aptos,Aptos_EmbeddedFont,Aptos_MSFontService,Calibri,Helvetica,sans-serif; font-size:12pt; color:rgb(0,0,0)\"><br></div></body></html>"

# Parse the HTML
soup = BeautifulSoup(html_string, 'html.parser')

# Get the text content
text_content = soup.get_text()

print(text_content)