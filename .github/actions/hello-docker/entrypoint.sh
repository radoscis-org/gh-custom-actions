#!/bin/sh -l


# Communicate with gh runner machine instead of core package
# Log sth into output in specific output
# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions
# Applies to any language
echo "::debug ::Our Debug Message"
echo "::warning ::Our Warning Message"
echo "::error ::Our Error Message"

echo "::add-mask::$1"
echo "Hello $1"

time=$(date)
echo "::set-output name=time::${time}"

echo "::group::Some expandable logs"
echo "Some Stuff"
echo "Some Stuff"
echo "Some Stuff"
echo "Some Stuff"
echo "Some Stuff"
echo "::endgroup::"

# Export env variable
echo '::set-env name=HELLO::hello from docker'