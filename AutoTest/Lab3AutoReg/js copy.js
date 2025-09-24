console.log("Тест-скрипт")

        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('registrationForm');
            
            const arr = new Map();

            // Валидаторы для каждого поля
            const validators = {
                username: function(value) {
                    if (!value.trim()) return 'Имя обязательно для заполнения';
                    if (value.length < 2) return 'Имя должно содержать минимум 2 символа';
                    if (!/^[a-zA-Zа-яА-ЯёЁ\s]+$/.test(value)) return 'Имя может содержать только буквы и пробелы';
                    return null;
                },
                
                email: function(value) {
                    if (!value.trim()) return 'Email обязателен для заполнения';
                    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!emailRegex.test(value)) return 'Введите корректный email адрес';
                    return null;
                },
                
                phone: function(value) {
                    if (!value.trim()) return 'Телефон обязателен для заполнения';
                    const phoneRegex = /^(\+7|8)[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$/;
                    if (!phoneRegex.test(value.replace(/\s/g, ''))) {
                        return 'Введите корректный номер телефона (формат: +7 XXX XXX XX XX)';
                    }
                    return null;
                },
                
                textarea: function(value) {
                    if (!value.trim()) return 'Сообщение обязательно для заполнения';
                    if (value.length < 10) return 'Сообщение должно содержать минимум 10 символов';
                    if (value.length > 500) return 'Сообщение не должно превышать 500 символов';
                    return null;
                },
                
                password: function(value) {
                    if (!value.trim()) return 'Пароль обязателен для заполнения';
                    if (value.length < 8) return 'Пароль должен содержать минимум 8 символов';
                    if (!/[A-Z]/.test(value)) return 'Пароль должен содержать хотя бы одну заглавную букву';
                    if (!/[0-9]/.test(value)) return 'Пароль должен содержать хотя бы одну цифру';
                    if (!/[!@#$%^&*]/.test(value)) return 'Пароль должен содержать хотя бы один специальный символ (!@#$%^&*)';
                    return null;
                }
            };

            // Функция для отображения ошибки
            function showError(input, message) {
                const errorElement = document.getElementById(input.id + '-error');
                errorElement.textContent = message;
                arr.set(input.id,message);
                input.classList.add('is-invalid');
                input.classList.remove('is-valid');
            }

            // Функция для очистки ошибки
            function clearError(input) {
                const errorElement = document.getElementById(input.id + '-error');
                errorElement.textContent = '';
                arr.delete(input.id);
                input.classList.remove('is-invalid');
                input.classList.add('is-valid');
            }

            // Валидация отдельного поля
            function validateField(input) {
                const validator = validators[input.name];
                if (validator) {
                    const error = validator(input.value);
                    if (error) {
                        showError(input, error);
                        return false;
                    } else {
                        clearError(input);
                        return true;
                    }
                }
                return true;
            }

            // Валидация всей формы
            function validateForm() {
                let isValid = true;
                const inputs = form.querySelectorAll('input, textarea');
                
                inputs.forEach(input => {
                    if (!validateField(input)) {
                        isValid = false;
                    }
                });
                
                return isValid;
            }

            // Обработчики событий
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                if (validateForm()) {
                    // Форма валидна, можно отправлять данные
                    document.getElementById('complete').textContent="Форма успешно отправлена!";

                    console.log('Данные формы:', {
                        username: document.getElementById('username').value,
                        email: document.getElementById('email').value,
                        phone: document.getElementById('phone').value,
                        message: document.getElementById('textarea').value,
                        password: document.getElementById('password').value
                    });
                }else{
                    for (let value of arr.values()) {
                        document.getElementById('complete').textContent="";
                        console.log(value)
                        document.getElementById('complete').textContent+=value+"\n";
                    }
                }
            });
        });