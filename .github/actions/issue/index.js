const core = require('@actions/core');
const github = require('@actions/github');

try {
  const token = core.getInput('token')
  const title = core.getInput('title')
  const body = core.getInput('body')
  const assignees = core.getInput('assignees')

  const octokit = github.getOctokit()
  //const octokit = new github.GitHub(token)
  const response = octokit.issues.create(
    {
      owner: github.context.repo.owner ,
      repo: github.context.repo.repo,
      // ..github.context.repo
      title: title,
      body: body,
      assignees: assignees ? assignees.split(","): undefined
    }
  )

  core.setOutput('issue', JSON.stringify(response.data))
} catch (error) {
    core.setFailed(error.message)
}



