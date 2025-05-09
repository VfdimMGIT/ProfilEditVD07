from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Для flash-сообщений

# Пример данных пользователя
user_data = {
    "name": "Иван Иванов",
    "email": "ivan@example.com",
    "password": "old_password_123"  # В реальном приложении храните хеш!
}


@app.route('/')
def home():
    return redirect(url_for('edit_profile'))  # Перенаправляем на страницу редактирования


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_email = request.form.get('email')
        new_password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not new_name or not new_email:
            flash("Имя и почта не могут быть пустыми!", "error")
        elif new_password and new_password != confirm_password:
            flash("Пароли не совпадают!", "error")
        else:
            user_data["name"] = new_name
            user_data["email"] = new_email
            if new_password:
                user_data["password"] = new_password  # Здесь должен быть хеш!

            flash("Профиль успешно обновлен!", "success")
            return redirect(url_for('edit_profile'))

    return render_template('profile_edit.html', user=user_data)


if __name__ == '__main__':
    app.run(debug=True)
