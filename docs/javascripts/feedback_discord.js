document.getElementById('feedback-form').addEventListener('submit', async function(e) {
  e.preventDefault()

  const feedbackText = document.getElementById('feedback-text').value
  const messageDiv = document.getElementById('feedback-message')

  try {
    const response = await fetch('https://discord.com/api/webhooks/1343158875817381898/lzriSPOQ-tOc6xUP_Pt55winuGyEqmQXY2FO9HbEUjXDwwayR3fSOz0YvceXXjYOhsi3', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
         content: feedbackText,
        // text: feedbackText,
        // page: window.location.href,
        // timestamp: new Date().toLocaleString('uk-UA')
      })
    })

    if (response.ok) {
      messageDiv.style.display = 'block'
      messageDiv.style.backgroundColor = '#c8e6c9'
      messageDiv.style.color = '#2e7d32'
      messageDiv.textContent = '✓ Дякую за відгук!'
      document.getElementById('feedback-form').reset()
    } else {
      throw new Error('Помилка сервера')
    }
  } catch (error) {
    messageDiv.style.display = 'block'
    messageDiv.style.backgroundColor = '#ffcdd2'
    messageDiv.style.color = '#c62828'
    messageDiv.textContent = '✗ Помилка при відправці. Спробуйте пізніше.'
  }
})

