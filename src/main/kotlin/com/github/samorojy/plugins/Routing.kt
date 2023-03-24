package com.github.samorojy.plugins

import io.ktor.server.application.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import java.io.File

suspend fun executeChecker(code: String): String = withContext(Dispatchers.IO) {
    val process = ProcessBuilder(
        "python3", "plagiarism_checker.py", code
    ).directory(File("src/main/python/com/github/samorojy/")).start()
    process.waitFor()
    String(process.inputStream.readBytes()).trim()
}

fun Application.configureRouting() {

    routing {
        get("/") {
            call.respondText("Hello World! I am an extraordinary code checker for similarity!")
        }
    }

    routing {
        post("/check") {
            // It can be a json or any other query body. But for simplicity, the full body is used.
            val requestBody = call.receive<String>()
            val output = executeChecker(requestBody)
            call.respondText(output)
        }
    }
}
