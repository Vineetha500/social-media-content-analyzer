const API_URL =
  import.meta.env.VITE_API_URL ||
  "http://localhost:8000";


export async function analyzeFile(file) {

  const formData = new FormData();

  formData.append("file", file);

  const response = await fetch(
    `${API_URL}/api/analyze`,
    {
      method: "POST",
      body: formData,
    }
  );

  let data;

  try {
    data = await response.json();
  } catch {
    throw new Error(
      "The server returned an invalid response."
    );
  }

  if (!response.ok) {
    throw new Error(
      data.detail ||
      "Unable to analyze the file."
    );
  }

  return data;
}