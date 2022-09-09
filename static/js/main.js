function setRemoveModalEventID(eventId) {
    const modalHiddenInput = document.getElementById('eventId');
    modalHiddenInput.setAttribute('value', eventId);
}

/*const navBtns = document.querySelectorAll('.link');
for (const btn of navBtns){
    btn.addEventListener('click', evt => {
       navBtns.forEach(nav => {
          nav.classList.remove('active');
       });
       evt.preventDefault();
       btn.classList.add('active');
    });
}*/