/* ################################## HEADER Dropdown menu ################################## */

let buttonShowMenu = document.querySelector('.button-show-menu');
let dropdownMenuXs = document.querySelector('.dropdown-menu-xs');
let headerWrapper = document.querySelector('.header-wrapper');
let containerFluid = document.querySelector('.container-fluid');

let showMenu = () => {
  dropdownMenuXs.classList.remove('visually-hidden');
  headerWrapper.classList.remove('rounded-bottom');
  headerWrapper.style.borderEndEndRadius = 0;
  headerWrapper.style.borderEndStartRadius = 0.375 + 'rem';

  let dropdownMenuItems = document.querySelectorAll('.dropdown-menu-xs-item');
  let clickDropdownMenuItemsHandler = (item) => {
    item.addEventListener('click', closeMenu)
  }

  for (let item of dropdownMenuItems) {
    clickDropdownMenuItemsHandler(item);
  }
}

let closeMenu = () => {
  dropdownMenuXs.classList.add('visually-hidden');
  headerWrapper.classList.add('rounded-bottom');
  headerWrapper.style.removeProperty('borderEndEndRadius');
  headerWrapper.style.removeProperty('borderEndStartRadius');
}

buttonShowMenu.addEventListener('click', (evt) => {
  evt.preventDefault()
  if (dropdownMenuXs.classList.contains('visually-hidden')) {
    showMenu();
  } else {
    closeMenu();
  }
})



/* ################################## END HEADER Dropdown menu ################################## */