
# Statsy AI

Querying CSV and Plotting Graphs using LLM(Llama2)

## Overview

Statsy AI is a web application designed to facilitate data visualization and analysis through the seamless integration of frontend and backend technologies. Leveraging React with Vite for the frontend and Flask for the backend, this project empowers users to upload CSV files, query their data, and generate insightful plots with ease.

## Key Features

- **User-friendly Interface:** The frontend interface, built using React and Vite, offers an intuitive and responsive user experience.
- **CSV File Upload:** Users can upload CSV files containing their dataset directly through the web interface.
- **Plot Generation:** Leveraging the Llama2 model, the backend generates insightful plots dynamically based on user-defined criteria.
- **Interactive Visualization:** The generated plots are interactive and customizable, allowing users to explore specific data points of interest.

## Technologies Used

- **Frontend:**
  - React
  - Vite
  - HTML/CSS

- **Backend:**
  - Flask
  - Python
  - Llama2

## Installation

To run the project locally, follow these steps:

- I have taken the sample video by running it in my college System with Specigfications Intel i5 processor and Nvidia RTX 4080 GPU.
- This will run only with these Specification to get faster inference.

1. Clone the repository:

   ```bash
   git clone https://github.com/abinashlingank/Statsy-AI.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Statsy-AI/llama
   ```

3. Install dependencies for both frontend and backend:

   ```bash
   # Install frontend dependencies
   cd frontend
   npm install

   # Install backend dependencies
   cd ..
   pip install -r requirements.txt
   ```
4. Installing the llama2 model using the following instructions.

## step 1:
- Visit the AI at Meta website, accept our License and submit the form. Once your request is approved, you will receive a pre-signed URL in your email.
## step 2:
- Ensure that your in the directory named `llama` or use this command `cd llama`
- Run the following command
```bash
./download.sh
```
- Launch the download.sh script (sh download.sh). When prompted, enter the presigned URL you receive in your email.
- Choose the model variant you want to download, for example: 7b-chat. This will download the tokenizer.model, and a directory llama-2-7b-chat with the weights in it.
## step 3:
Run the following to create a link to the tokenizer. This is needed for conversion (next step)
```bash
ln -h ./tokenizer.model ./llama-2-7b-chat/tokenizer.model 
```

## step 4:
Convert the model weights to run with Hugging Face:

```bash
TRANSFORM=`python -c "import transformers;print('/'.join(transformers.  __file__.split('/')[:-1])+'/models/llama/convert_llama_weights_to_hf.py')"`
pip install protobuf && python $TRANSFORM --input_dir ./llama-2-7b-chat --model_size 7B --output_dir ./llama-2-7b-chat-hf
   ```
5. Start the development servers:

   ```bash
   # Start the frontend server
   cd frontend
   npm run dev

   # Start the backend server
   cd ..
   python3 app.py
   ```

5. Access the application in your web browser at `http://localhost:5173`.

## Usage

1. Upload a CSV file containing your dataset through the web interface.
2. Generate plots based on your selected criteria.
3. Interact with the plots to explore specific data points or trends.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thank you to the creators of React, Vite, Flask and other open-source tools used in this project.
- Special thanks to the Llama2 model developers for their contributions to data analysis and visualization.
