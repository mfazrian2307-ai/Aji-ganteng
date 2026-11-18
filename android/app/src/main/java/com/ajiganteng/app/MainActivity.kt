package com.ajiganteng.app

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.widget.*

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(24, 24, 24, 16)
            setBackgroundColor(Color.rgb(255, 245, 248))
        }

        val title = TextView(this).apply {
            text = "💕 AJI GANTENG"
            textSize = 25f
            setTextColor(Color.rgb(220, 40, 110))
            gravity = Gravity.CENTER
        }

        val subtitle = TextView(this).apply {
            text = "Hai sayang, aku di sini buat kamu ❤️"
            textSize = 16f
            gravity = Gravity.CENTER
            setPadding(0, 16, 0, 24)
        }

        val chat = TextView(this).apply {
            text = "Aji: Akhirnya kamu datang juga, sayang 😘"
            textSize = 17f
            setPadding(12, 20, 12, 20)
        }

        val input = EditText(this).apply {
            hint = "Ketik pesan untuk Aji..."
            textSize = 16f
        }

        val send = Button(this).apply {
            text = "Kirim ❤️"
            setOnClickListener {
                val message = input.text.toString().trim()
                if (message.isNotEmpty()) {
                    chat.text = "Kamu: $message\n\nAji: Pesanmu sudah aku terima, sayang ❤️"
                    input.text.clear()
                }
            }
        }

        root.addView(title)
        root.addView(subtitle)
        root.addView(chat, LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, 0, 1f
        ))
        root.addView(input)
        root.addView(send)

        setContentView(root)
    }
}
