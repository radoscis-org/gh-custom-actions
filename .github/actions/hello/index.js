const core = require('@actions/core');
const github = require('@actions/guthub');



try {
    const name = core.getInput('who-to-greet');
    console.log('Hello ${name}');

    const time = new Date();
    core.setOutput("time", time.toTimeString());

    console.log(JSON.stringify(github, null,'\t'))

    throw(new Error("Some Error Message"))

} catch (error) {
    core.setFailed(error.message)
}



