# Відгук

<div id="feedbackMessage" style="display: none; padding: 12px; border-radius: 4px; margin-bottom: 15px; font-weight: bold;"></div>

<form id="feedbackForm">
  <div style="margin-bottom: 15px;">
    <label for="feedbackEmail">Email:</label>
    <input type="email" id="feedbackEmail" placeholder="your@email.com" required style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;">
  </div>
  
  <div style="margin-bottom: 15px;">
    <label for="feedbackText">Ваш відгук:</label>
    <textarea id="feedbackText" placeholder="Ваш відгук..." required style="width: 100%; height: 150px; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;"></textarea>
  </div>
  
  <div style="margin-bottom: 15px;">
    <label for="feedbackFile">Скріншот (опціонально):</label>
    <input type="file" id="feedbackFile" accept="image/*" style="padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
    <small style="display: block; margin-top: 5px;">Можна також вставити скріншот через Ctrl+V</small>
    <div id="fileStatus" style="margin-top: 8px; font-size: 0.9em; color: #666;"></div>
  </div>
  
  <button type="submit" style="padding: 10px 20px; background-color: #5865F2; color: white; border: none; border-radius: 4px; cursor: pointer;">Відправити</button>
</form>

<script>
const webhookUrl = 'https://discord.com/api/webhooks/__DISCORD_WEBHOOK_ID__/__DISCORD_WEBHOOK_TOKEN__';
let selectedFile = null;

function showMessage(text, isSuccess) {
  const messageEl = document.getElementById('feedbackMessage');
  messageEl.textContent = text;
  messageEl.style.backgroundColor = isSuccess ? '#d4edda' : '#f8d7da';
  messageEl.style.color = isSuccess ? '#155724' : '#721c24';
  messageEl.style.display = 'block';
  
  setTimeout(() => {
    messageEl.style.display = 'none';
  }, 4000);
}

function updateFileStatus() {
  const fileStatus = document.getElementById('fileStatus');
  if (selectedFile) {
    fileStatus.textContent = `✅ Файл готовий: ${selectedFile.name}`;
    fileStatus.style.color = '#28a745';
  } else {
    fileStatus.textContent = '';
  }
}

// Обробка вибору файлу
document.getElementById('feedbackFile').addEventListener('change', (e) => {
  selectedFile = e.target.files[0];
  updateFileStatus();
});

// Обробка вставки скріншота через Ctrl+V
document.addEventListener('paste', (e) => {
  const items = e.clipboardData?.items;
  if (!items) return;
  
  for (let item of items) {
    if (item.type.startsWith('image/')) {
      selectedFile = item.getAsFile();
      document.getElementById('feedbackFile').value = '';
      updateFileStatus();
      break;
    }
  }
});

document.getElementById('feedbackForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const email = document.getElementById('feedbackEmail').value;
  const text = document.getElementById('feedbackText').value;
  const submitButton = e.target.querySelector('button[type="submit"]');
  
  submitButton.disabled = true;
  submitButton.textContent = 'Відправляю...';
  
  const formData = new FormData();
  
  // Основне повідомлення
  const payload = {
    content: `📝 **Новий відгук від ${email}:**\n\n${text}`
  };
  
  formData.append('payload_json', JSON.stringify(payload));
  
  // Додати скріншот якщо він є
  if (selectedFile) {
    formData.append('files[0]', selectedFile, selectedFile.name);
  }
  
  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      body: formData
    });
    
    if (response.ok) {
      showMessage('✅ Дякуємо за відгук!', true);
      document.getElementById('feedbackEmail').value = '';
      document.getElementById('feedbackText').value = '';
      document.getElementById('feedbackFile').value = '';
      selectedFile = null;
      updateFileStatus();
    } else {
      showMessage('❌ Помилка при відправці. Спробуйте пізніше.', false);
    }
  } catch (error) {
    console.error(error);
    showMessage('❌ Помилка з\'єднання', false);
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = 'Відправити';
  }
});
</script>
