<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>About Page</title>
</head>

<body>
    <h1>About Us</h1>
    <ul>
        {% for member in team_members %}
            <li>{{ member.full_name }} (ID: {{ member.student_id }}) - Email: {{ member.email }}</li>
        {% endfor %}
    </ul>
</body>

</html>
