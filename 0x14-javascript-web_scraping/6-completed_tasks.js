#!/usr/bin/node

const request = require("request");

const url = process.argv[2];

request(url, function(error, response, body) {
  if (error) {
    console.error(error);
  } else {
    let tasks = JSON.parse(body);
    let userTasks = {};

    tasks.forEach(function(task) {
      if (task.completed) {
        if (!userTasks[task.userId]) {
          userTasks[task.userId] = 0;
        }
        userTasks[task.userId]++;
      }
    });

    for (let userId in userTasks) {
      console.log(`User ID: ${userId} Completed Tasks: ${userTasks[userId]}`);
    }
  }
});

