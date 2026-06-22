# Feedback

Надішліть нам ваш відгук:

<form id="feedback-form" class="feedback-form">
  <div class="form-group">
    <label for="feedback-text">Ваш відгук:</label>
    <textarea 
      id="feedback-text" 
      name="feedback-text" 
      rows="6" 
      placeholder="Напишіть ваш відгук тут..." 
      required
    ></textarea>
  </div>
  
  <button type="submit" class="md-button md-button--primary">
    Відправити
  </button>
  
  <div id="feedback-message" style="display: none; margin-top: 1rem; padding: 1rem; border-radius: 4px;"></div>
</form>


<style>
.feedback-form {
  max-width: 600px;
  margin: 2rem 0;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-family: inherit;
  font-size: inherit;
}

.form-group textarea:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
}
</style>
