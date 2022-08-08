const core = require('@actions/core');
const github = require('@actions/github');



try {

    // will appear if debugging is enabled (secret ACTIONS_STEP_DEBUG=true)
    core.debug('Debug message')
    core.warning('Warining message')
    core.error('Error message')

    const name = core.getInput('who-to-greet');
    core.setSecret('MAskedStringInLogs')
    console.log('Hello ', name);



    const time = new Date();
    core.setOutput("time", time.toTimeString());

    core.startGroup('Logging GITHUB OBJECT')
    console.log(JSON.stringify(github, null,'\t'))
    core.endGroup()

    core.exportVariable('HELLO','hello man!')

} catch (error) {
    core.setFailed(error.message)
}



