function home() {
    window.location.href = "homepage.html"
}

const msg = document.getElementById('msg')
msg.style.display = "none"

var arr = []
const button = document.getElementById('button')
button.addEventListener('click', (e) => {
    e.preventDefault()

    if (document.getElementById('input').value == "") {
        msg.style.display = "block"
        msg.textContent = "Campo de cadastro vazio! Preencha-o e tente novamente."
    } else {

        if (localStorage.ativ) {
            arr = JSON.parse(localStorage.ativ)
        }
        const input = document.getElementById('input').value
        arr.push(input)
        document.getElementById('input').value = ""
        localStorage.ativ = JSON.stringify(arr)
    }
})



console.log(JSON.parse(localStorage.ativ))