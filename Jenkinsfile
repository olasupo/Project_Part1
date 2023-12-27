pipeline {
    agent any

    stages {
        stage('Fetch Source Code From Git...') {
            steps {
                git branch: 'master', url: 'https://github.com/olasupo/DevNetLab.git'
            }
        }

        stage('Initialize Ansible...') {
            steps {
                script {
                    def tfHome = tool name: 'ansible'
                    env.PATH = "${tfHome}:${env.PATH}"
                    sh 'ansible --version'
                }
            }
        }

        stage('Network Configuration Using Ansible...') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh "ansible-playbook DevNet_Lab/jautomator.yml -i DevNet_Lab/hosts --vault-password-file ./vpass"
                }
            }
        }

        stage('Run Tests Using Ansible...') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('UNSTABLE') }
            }

            steps {
                echo 'Congratulations!!! Your Network has been Successfully Configured...'
                echo 'Testing will start in a moment...'
                echo 'Please wait while the network converges before commencement of tests...'
                sleep 20
                
                sh "ansible-playbook DevNet_Lab/tests.yml -i DevNet_Lab/hosts --vault-password-file ./vpass"
            }
        }
    }

    post {
        failure {
            script {
                // Retrieve the last 1000 characters of the build log
                def buildLog = currentBuild.rawBuild.getLog(1000)

                // Parse the log for fatal errors and ask ChatGPT for solutions
                def rootCause = parseLogForRootCause(buildLog)

                echo "This is the Root cause: ${rootCause}"

                echo "Please wait while we analyze the failure cause..."
                def chatGptResponse = askChatGpt(rootCause)

                // Extract the relevant information from the ChatGPT response
                def chatGptSuggestions = extractChatGptSuggestions(chatGptResponse)

                // Add code to send failure email notification with ChatGPT suggestions
                emailext subject: 'FAILURE IN PIPELINE EXECUTION',
                        body: """
                          Hello Dear,

                          The pipeline encountered some errors during execution. Please find the detailed Root cause as follows:

                          ${rootCause}

                          Here are some suggested solutions:
                          ${chatGptSuggestions}

                          Regards,
                          Jenkins
                          """,
                        to: 'olasupo.o@gmail.com'
            }
        }
        success {
            script {
                // Add code to send success email notification
                emailext subject: 'SUCCESS IN PIPELINE EXECUTION',
                        body: """
                          Hello Dear,

                          Congratulations, The pipeline execution was successful. You can proceed to accept the new infrastructure.

                          Regards,
                          Jenkins
                          """,
                        to: 'bubblntechnologies@gmail.com'
            }
        }
    }
}

def askChatGpt(question) {
    def openai_key = "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"

    // Escape double-quotes within the question
    def escapedQuestion = question.replaceAll('"', '\\"')

    def prompt = "Please analyze this Jenkins console failure output encountered while trying to setup a network: ${escapedQuestion} and provide some explanation and detailed troubleshooting steps on how to resolve it; please ensure troubleshooting steps begin with most likely problem to least likely."

    def payloadMap = [
            prompt: prompt,
            max_tokens: 3000,
            n: 1,
            stop: null,
            temperature: 1.0
    ]

    def payload = groovy.json.JsonOutput.toJson(payloadMap)

    def response = sh(
            script: """
        curl -X POST -H 'Content-Type: application/json' \\
        -H 'Authorization: Bearer ${openai_key}' \\
        -d '${payload}' \\
        https://api.openai.com/v1/engines/text-davinci-003/completions > response.json
        """,
            returnStatus: true
    )

    if (response == 0) {
        def responseBody = readFile('response.json')
        return responseBody ?: "Failed to get a valid response from ChatGPT"
    } else {
        return "An error was encountered while calling the AI engine. cURL command failed with status code: ${response}"
    }
}

def parseLogForRootCause(logList) {
    def log = logList.join('\n')
    def errorLines = log.readLines().findAll { it.contains('ERROR') || it.contains('fatal') }
    return errorLines ? errorLines.join('\n') : log.tokenize('\n').last()
}

def extractChatGptSuggestions(chatGptResponse) {
    try {
        def responseJson = readJSON text: chatGptResponse
        def suggestions = responseJson?.choices?.collect { it?.text }?.join('\n')
        return suggestions ?: "No valid suggestions found in ChatGPT response."
    } catch (Exception e) {
        return "Error extracting ChatGPT suggestions."
    }
}

