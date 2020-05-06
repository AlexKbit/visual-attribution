function previewFile() {
  var preview = document.getElementById('preview');
  var file = document.getElementById('inputImg').files[0];
  var reader = new FileReader();

  reader.onloadend = function () {
    preview.src = reader.result;
  }

  if (file) {
    reader.readAsDataURL(file);
  } else {
    preview.src = "";
  }

  document.getElementById('dress_type').innerHTML = 'Dress type: ?';
  document.getElementById('material').innerHTML = 'Material: ?';
  document.getElementById('length').innerHTML = 'Length: ?';
  document.getElementById('color').innerHTML = 'Color: ?';
}

function sendImage() {
    var fd = new FormData;
    fd.append('image', document.getElementById('inputImg').files[0]);
    $.ajax({
        type: "POST",
        url: "/predict",
        data: fd,
        processData: false,
        contentType: false,
        success: function(result){
            console.info(result);
            data = JSON.parse(result);
            document.getElementById('dress_type').innerHTML = 'Dress type: ' + data.dress_type;
            document.getElementById('material').innerHTML = 'Material: ' + data.material;
            document.getElementById('length').innerHTML = 'Length: ' + data.length;
            document.getElementById('color').innerHTML = 'Color: ' + data.color;
        }
    });
}