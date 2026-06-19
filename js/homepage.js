function home() {
    window.location.href = "homepage.html"
}
function ca() {
    window.location.href = "registerPage.html"
} function kan() {
    window.location.href = "kanban.html"
}

const relBtn = document.getElementById('relBtn')
relBtn.addEventListener("click", (e) => {
    e.preventDefault()

    const content = JSON.parse(localStorage.ativ)
    const blob = new Blob([content], {type:"text/plain"})
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = "relatorioKanban.txt" 
    a.click()
})