
const btn = document.querySelector('button');
const main = document.querySelector('.container');
const url = 'engineering.txt';

btn.onclick = reqData;

function output(data){
    main.innerHTML = this.responseText
}

function reqData(){
    const xhr = new XMLHttpRequest();
    xhr.addEventListener('load', output)
    xhr.open('GET', url);
    xhr.send();

}