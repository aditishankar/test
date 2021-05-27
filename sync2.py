import git, os, shutil

# local version of airflow
test = git.Repo('.')
# official version of airflow - cloned locally as apache-airflow
airflow = git.Repo('../apache-airflow')
fetch = airflow.remotes.origin.fetch()[0]
print(fetch)
pull = airflow.remotes.origin.pull()
print(pull)
# at = test.create_remote('at', "https://github.com/apache/airflow.git")
at = test.remotes['at']
at.fetch()
# at.pull(at.refs[0].remote_head)
test.git.pull("at", "master", "--allow-unrelated-histories")
test.git.add("-A")
test.index.commit("syncing master")
at.push()
#test.git.push("origin", "test")


print("---- DONE ----")

