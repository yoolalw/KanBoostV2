function home() {
    window.location.href = "homepage.html"
}

var arr = []
const button = document.getElementById('button')
button.addEventListener('click', (e) => {
    e.preventDefault()

    if(localStorage.ativ){
        arr = JSON.parse(localStorage.ativ)
    }
    const input = document.getElementById('input').value
    arr.push(input)
    document.getElementById('input').value = ""
    localStorage.ativ = JSON.stringify(arr)
})

console.log(JSON.parse(localStorage.ativ))