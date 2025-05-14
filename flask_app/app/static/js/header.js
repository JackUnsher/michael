// JavaScript для функциональности хедера

document.addEventListener('DOMContentLoaded', function() {
    // Функция для мобильного меню
    const hamburger = document.querySelector('.hamburger');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (hamburger && mobileMenu) {
        hamburger.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');
            // Анимация гамбургер-меню
            const spans = hamburger.querySelectorAll('span');
            spans.forEach(span => span.classList.toggle('active'));
            
            if (mobileMenu.classList.contains('active')) {
                // Если меню открыто, добавляем стили для анимации гамбургера в крестик
                spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
            } else {
                // Возвращаем гамбургер в исходное состояние
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
        
        // Закрываем мобильное меню при клике на пункт меню
        const mobileMenuLinks = mobileMenu.querySelectorAll('a');
        mobileMenuLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.remove('active');
                // Возвращаем гамбургер в исходное состояние
                const spans = hamburger.querySelectorAll('span');
                spans.forEach(span => {
                    span.classList.remove('active');
                    span.style.transform = 'none';
                    span.style.opacity = '1';
                });
            });
        });
    }
    
    // Функция для работы языкового селектора
    const langSelector = document.querySelector('.lang-selector');
    if (langSelector) {
        const langCurrent = langSelector.querySelector('.lang-selector__current');
        const langDropdown = langSelector.querySelector('.lang-selector__dropdown');
        
        // Обработка клика на текущий язык (для мобильных устройств)
        if (langCurrent) {
            langCurrent.addEventListener('click', function(e) {
                e.stopPropagation();
                langDropdown.style.display = langDropdown.style.display === 'block' ? 'none' : 'block';
            });
        }
        
        // Закрываем дропдаун при клике в любое место страницы
        document.addEventListener('click', function() {
            if (langDropdown) {
                langDropdown.style.display = 'none';
            }
        });
        
        // Предотвращаем закрытие дропдауна при клике внутри него
        if (langDropdown) {
            langDropdown.addEventListener('click', function(e) {
                e.stopPropagation();
            });
        }
    }
    
    // Обработка активного пункта меню
    const navLinks = document.querySelectorAll('.nav__link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Удаляем активный класс у всех пунктов меню
            navLinks.forEach(l => l.parentElement.classList.remove('nav__item--active'));
            // Добавляем активный класс текущему пункту
            this.parentElement.classList.add('nav__item--active');
        });
    });
});
