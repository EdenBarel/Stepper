// Selectors
document.querySelector('form[data-form="form-1"]').addEventListener('submit', handelUsenameForm);
document.querySelector('form[data-form="form-2"]').addEventListener('submit', handelRandomForm);
document.getElementById('form-2').style.visibility="hidden";



// Event Handlers
function handelUsenameForm(e) {
    e.preventDefault();
    const API_URL_RANDOM = "http://127.0.0.1:8000/vanilla-app/get-random/"
    var letters = /^[A-Za-z]+$/;
    let username_input = document.querySelector('input[name="name"]');
    let user_random_input = document.querySelector('input[name="rand"]');
    var step2 = document.getElementById("step2");
    if(!username_input.value.match(letters)){
          alert('Please input alphabet characters only', 'Error', 'error');
          username_input.value = "";
          return false;
    }
    document.getElementById('form-2').style.visibility="visible";
    axios
    .get(API_URL_RANDOM+username_input.value)
    .then(res=>{
        user_random_input.value = res.data;
        
    });
    step2.className="active";

}

function handelRandomForm (e){
    e.preventDefault();
    let random_string_input = document.querySelector('input[name="rand"]');
    let user_random_input_check = document.querySelector('input[name="randomStr"]');
    let status = document.querySelector('input[name="stat"]');
    var step3 = document.getElementById("step3");
    const API_URL_IS_CORRECT_RANDOM = "http://127.0.0.1:8000/vanilla-app/is-correct-random/"
    const API_URL_GET_BINART_FILE = "http://127.0.0.1:8000/media/images/LightspinLogo.png"
    axios
    .get(API_URL_IS_CORRECT_RANDOM+random_string_input.value+"/"+user_random_input_check.value)
    .then(res=>{
      if(res.data === "correct random string"){
        status.value = "Success!";
        axios({
          url: API_URL_GET_BINART_FILE,
          method: 'GET',
          responseType: 'blob'
        }).then((response)=>{
          var fileURL = window.URL.createObjectURL(new Blob([response.data]));
          var fileLink = document.createElement('a');
          fileLink.href = fileURL;
          fileLink.setAttribute('download', 'Lightspin.png');
          document.body.appendChild(fileLink);
          fileLink.click();
        });
      }
      else{
        console.log(res.data);
        status.value = "Error";
      }
    });
    step3.className="active";
}
