
![banner](./readme-resources/images/banner.png)

# About the project

Flask-Task is an application that allows you to manage your tasks quickly and optimally.
With this application, you can register users and assign tasks

# How to use the app?

First you need to make sure you have Docker and `docker-compose` installed on your PC.

In case you have these tools, the next thing you should do is open a terminal by positioning yourself in this directory, and execute the following command:

```bash
docker-compose up
```

This instruction creates and runs a container inside your PC with the application.

To use the app, you will access the following [URL](http://localhost:8000)

The routes you can access are the following:

### Tasks

+ /tasks
+ /tasks/info
+ /tasks/{id}
+ /tasks?completed={true|false}
+ /tasks?title={text}
+ /tasks?completed={true|false}&title={text}

### Users

+ /users
+ /users/{id}
+ /users/{id}/tasks
