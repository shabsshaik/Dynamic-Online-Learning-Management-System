const userName =document.querySelector('.user').innerHTML;
// const submitBtn = document.getElementById("submitBtn");

const { PDFDocument, rgb, degrees } = PDFLib;


const capitalize = (str, lower = false) =>
  (lower ? str.toLowerCase() : str).replace(/(?:^|\s|["'([{])+\S/g, (match) =>
    match.toUpperCase()
  );

  window.addEventListener("load", () => {
    const val = capitalize(userName);

  //check if the text is empty or not
  if (val.trim() !== "" ) {
    generatePDF(val);
  }
   else {
    userName.reportValidity();
  }
});


const generatePDF = async (name) => {
  const existingPdfBytes = await fetch("/static/certificate.pdf").then((res) =>
    res.arrayBuffer()
  );

  // const fontBytes = await fetch("./Sanchez-Regular.ttf").then((res) =>
  // res.arrayBuffer()
  // );
  
  // Load a PDFDocument from the existing PDF bytes
  const pdfDoc = await PDFDocument.load(existingPdfBytes);
  //pdfDoc.registerFontkit(fontkit);


  // Embed our custom font in the document
  //const SanChezFont = await pdfDoc.embedFont(fontBytes);

  // Get the first page of the document
  const pages = pdfDoc.getPages();
  const firstPage = pages[0];
  // const sc = pages[0];


  // Draw a string of text diagonally across the first page
  firstPage.drawText(name, {
    x: 180,
    y: 230,
    size: 18,
    color: rgb(0,0,0),
  });

  // sc.drawText(name, {
  //   x: 200,
  //   y: 230,
  //   size: 18,
  //   color: rgb(0,0,0),
  // });

   const pdfDataUri = await pdfDoc.saveAsBase64({ dataUri: true });
   document.getElementById("pdf").src = pdfDataUri;
};