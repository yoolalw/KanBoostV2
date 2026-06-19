function home() {
    window.location.href = "homepage.html"
}
function ca() {
    window.location.href = "registerPage.html"
}

console.log(JSON.parse(localStorage.ativ))
const todo = document.getElementById('todo')
const doing = document.getElementById('doing')
const done = document.getElementById('done')

JSON.parse(localStorage.ativ).forEach(a => {
    const card = document.createElement('div')
    card.className = "atividade h-[120px] z-5 rounded-xl bg-white shadow-lg w-full flex justify-center align-middle items-center m-auto flex-col"
    card.innerHTML += `
        <h1 class="text-[30px] text-[#333]">${a}</h1>
        <div class="buttons flex gap-15 mt-5">
            <button id="voltar" class="voltar bg-blue-100 text-[15px] text-blue-800 border-blue-300  border-2 h-[30px] cursor-pointer rounded-full hover:bg-blue-300  w-[75px]">Voltar</button>
            <button id="avancar" class="avancar bg-blue-100 text-[15px] text-blue-800 border-blue-300 h-[30px] border-2 cursor-pointer  rounded-full hover:bg-blue-300 w-[75px]">Avançar</button>
        </div>
    `
    todo.appendChild(card)

})

const atividade = document.getElementById('atividade')

document.addEventListener('click', (e) => {
    e.preventDefault()
    const card = e.target.closest('.atividade')
    if (!card) return
    const listaAtt = card.parentElement
    if (e.target.classList.contains('avancar')) {
        if (listaAtt.id === 'todo') {
            doing.appendChild(card)
        } if (listaAtt.id === 'doing') {
            done.appendChild(card)
        }
    }   

    if (e.target.classList.contains('voltar')) {
        if (listaAtt.id === 'done') {
            doing.appendChild(card)
        } if (listaAtt.id === 'doing') {
            todo.appendChild(card)
        }
    }   
})
