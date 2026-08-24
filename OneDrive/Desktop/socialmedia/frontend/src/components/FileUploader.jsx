import { useRef, useState } from "react";
import {
  Upload,
  FileText,
  Image as ImageIcon,
  X,
} from "lucide-react";


export default function FileUploader({
  onAnalyze,
  loading,
}) {

  const inputRef = useRef(null);

  const [dragging, setDragging] =
    useState(false);

  const [selectedFile, setSelectedFile] =
    useState(null);

  const [error, setError] =
    useState("");


  const validateFile = (file) => {

    if (!file) {
      return false;
    }

    const allowedTypes = [
      "application/pdf",
      "image/png",
      "image/jpeg",
    ];

    const maxSize =
      10 * 1024 * 1024;

    if (!allowedTypes.includes(file.type)) {

      setError(
        "Only PDF, PNG and JPG files are supported."
      );

      return false;
    }

    if (file.size > maxSize) {

      setError(
        "File size must be less than 10 MB."
      );

      return false;
    }

    setError("");

    return true;
  };


  const selectFile = (file) => {

    if (!validateFile(file)) {
      return;
    }

    setSelectedFile(file);
  };


  const handleInputChange = (event) => {

    const file =
      event.target.files?.[0];

    selectFile(file);
  };


  const handleDrop = (event) => {

    event.preventDefault();

    setDragging(false);

    const file =
      event.dataTransfer.files?.[0];

    selectFile(file);
  };


  const handleAnalyze = () => {

    if (!selectedFile) {
      setError("Please select a file.");
      return;
    }

    onAnalyze(selectedFile);
  };


  const removeFile = () => {

    setSelectedFile(null);

    setError("");

    if (inputRef.current) {
      inputRef.current.value = "";
    }
  };


  return (
    <div className="upload-wrapper">

      <div
        className={`drop-zone ${
          dragging ? "dragging" : ""
        }`}
        onDragOver={(event) => {
          event.preventDefault();
          setDragging(true);
        }}
        onDragLeave={() => {
          setDragging(false);
        }}
        onDrop={handleDrop}
        onClick={() => {
          if (!selectedFile) {
            inputRef.current?.click();
          }
        }}
      >

        <input
          ref={inputRef}
          type="file"
          accept=".pdf,.png,.jpg,.jpeg"
          hidden
          onChange={handleInputChange}
        />

        {!selectedFile ? (
          <>
            <div className="upload-icon">
              <Upload size={38} />
            </div>

            <h3>
              Drop your document here
            </h3>

            <p>
              or click to browse your files
            </p>

            <span>
              PDF, PNG, JPG or JPEG · Max 10 MB
            </span>
          </>
        ) : (

          <div className="selected-file">

            <div className="file-icon">

              {selectedFile.type ===
              "application/pdf" ? (
                <FileText size={34} />
              ) : (
                <ImageIcon size={34} />
              )}

            </div>

            <div className="file-information">

              <strong>
                {selectedFile.name}
              </strong>

              <small>
                {(
                  selectedFile.size /
                  1024 /
                  1024
                ).toFixed(2)}{" "}
                MB
              </small>

            </div>

            <button
              className="remove-button"
              onClick={(event) => {
                event.stopPropagation();
                removeFile();
              }}
            >
              <X size={18} />
            </button>

          </div>
        )}

      </div>

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      <button
        className="analyze-button"
        disabled={!selectedFile || loading}
        onClick={handleAnalyze}
      >
        {loading
          ? "Analyzing..."
          : "Analyze Content"}
      </button>

    </div>
  );
}