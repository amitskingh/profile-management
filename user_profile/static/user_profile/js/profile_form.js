const eduContainer = document.getElementById("education-container");
const addEduBtn = document.getElementById("add-education");
const skillsContainer = document.getElementById("skills-container");
const addSkillBtn = document.getElementById("add-skill");

function createEducationField() {
  const div = document.createElement("div");
  div.className = "rounded-lg bg-gray-50 p-4";
  div.innerHTML = `
          <div>
            <label class="block text-sm font-medium text-gray-900">Institution Name</label>
            <div class="mt-2.5">
              <input type="text" name="education_name[]" placeholder="e.g. Harvard University"
                class="block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-blue-600" />
            </div>
          </div>
          <div class="mt-3">
            <label class="block text-sm font-medium text-gray-900">Field of Study</label>
            <div class="mt-2.5">
              <input type="text" name="education_field[]" placeholder="e.g. Computer Science"
                class="block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-blue-600" />
            </div>
          </div>
          <div class="mt-3">
            <label class="block text-sm font-medium text-gray-900">Percentage</label>
            <div class="mt-2.5">
              <input type="text" name="education_percentage[]" placeholder="e.g. 85%"
                class="block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-blue-600" />
            </div>
          </div>
          <button type="button" class="mt-4 px-4 py-2 bg-rose-600 text-white rounded-md hover:bg-rose-700 remove-edu">Remove</button>
        `;
  eduContainer.appendChild(div);
  div
    .querySelector(".remove-edu")
    .addEventListener("click", () => div.remove());
}

function createSkillField() {
  const div = document.createElement("div");
  div.className = "flex items-center gap-3";
  div.innerHTML = `
          <input type="text" name="skills[]" placeholder="Skill (e.g. JavaScript)"
            class="flex-1 rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-blue-600" />
          <button type="button" class="bg-rose-600 text-white rounded-md px-3 py-2 hover:bg-rose-700 remove-skill">Remove</button>
        `;
  skillsContainer.appendChild(div);
  div
    .querySelector(".remove-skill")
    .addEventListener("click", () => div.remove());
}

const form = document.getElementById("myFormId");
// Or using a class, name, or query selector
// const form = document.querySelector('form');

form.addEventListener("submit", function (event) {
  event.preventDefault();

  // Your form handling logic goes here
  handleFormDetails(event);
});

function handleFormDetails(event) {
  const formElement = event.target; // The form element that was submitted
  const formData = new FormData(formElement);

  for (const [key, value] of formData.entries()) {
    console.log(`${key}: ${value}`);
  }
}

addEduBtn.addEventListener("click", createEducationField);
addSkillBtn.addEventListener("click", createSkillField);
