# gh-custom-actions

## TOOLKIT for building custom acitons
https://github.com/actions/toolkit

npm i @actions/github --save
npm i @actions/core --save

## Running custom action
Not to push node_modules folder which is not a good practice
we will build our action in one file

eg. with "ncc"

npm i --save-dev @zeit/ncc

npx ncc build .github/actions/hello/index.js -o .github/actions/hello/dist

## Core package description
https://github.com/actions/toolkit/tree/master/packages/core

# Workflow commands for GithubActions
https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions