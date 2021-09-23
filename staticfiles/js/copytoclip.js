  function CopyToClipboard() {
  var copyText = document.getElementById('myInput')
  copyText.select();
  document.execCommand('copy')
  console.log('Copied Text')
}
