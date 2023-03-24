package com.github.samorojy

import com.github.samorojy.plugins.executeChecker
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.withContext
import java.io.File
import kotlin.test.Test
import kotlin.test.assertEquals


class ApplicationTest {
    // can only be launched with the database running
    // Also there could be the tokenization tests but pygmentize returns tokens in random order
    /*@Test
    fun plagiarismTrueTest() {
        val codeToCheck = javaClass.classLoader.getResource("KtConfigurator.txt")?.readText()
        val correctAnswer =
            """educational-plugin-master\educational-plugin-master\Edu-Kotlin\src\com\jetbrains\edu\kotlin\KtConfigurator.kt"""
        codeToCheck?.let {
            runBlocking {
                assertEquals(correctAnswer, executeChecker(it))
            }
        }
    }

    @Test
    fun plagiarismFalseTest() {
        val codeToCheck = javaClass.classLoader.getResource("PyHelloWorld.txt")?.readText()
        val correctAnswer = "OK"
        codeToCheck?.let {
            runBlocking {
                assertEquals(correctAnswer, executeChecker(it))
            }
        }
    }*/
}
