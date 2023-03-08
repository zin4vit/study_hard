function correct() {
    var correctButton = document.getElementById('correct')
    const wrapper = document.createElement('div')
    wrapper.className = 'al'
    wrapper.innerHTML = [
`<div class="alert alert-success alert-dismissible" role="alert">`,
`   <div>Правильно</div>`,
'   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
'</div>'
].join('')
    correctButton.append(wrapper)
    setTimeout(function () {
        wrapper.remove();
    }, 2000)
}
function incorrect() {
    var incorrectButton = document.getElementById('incorrect')
    const wrapper = document.createElement('div')
    wrapper.className = 'al'
    wrapper.innerHTML = [
`<div class="alert alert-danger alert-dismissible" role="alert">`,
`   <div>Попробуйте ещё раз!</div>`,
'   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
'</div>'
].join('')
    incorrectButton.append(wrapper)
    setTimeout(function () {
        wrapper.remove();
    }, 2000)
}