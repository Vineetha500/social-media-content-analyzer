import { useState } from "react";

import {
  BarChart3,
  Sparkles,
  ShieldCheck,
} from "lucide-react";

import FileUploader from "./components/FileUploader";
import AnalysisResult from "./components/AnalysisResult";
import LoadingSpinner from "./components/LoadingSpinner";

import { analyzeFile } from "./services/api";


export default function App() {

  const [result, setResult] =
    useState(null);

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");


  const handleAnalyze = async (file) => {

    setLoading(true);
    setError("");
    setResult(null);

    try {

      const data =
        await analyzeFile(file);

      setResult(data);

    } catch (error) {

      setError(
        error.message ||
        "Something went wrong."
      );

    } finally {

      setLoading(false);

    }
  };


  const handleReset = () => {

    setResult(null);
    setError("");

  };


  return (
    <div className="app">

      <header className="navbar">

        <div className="brand">

          <div className="brand-icon">
            <BarChart3 size={22} />
          </div>

          <span>
            ContentAnalyzer
          </span>

        </div>

        <div className="navbar-badge">
          <ShieldCheck size={15} />
          Secure analysis
        </div>

      </header>


      <main>

        {!result && !loading && (

          <section className="hero">

            <div className="hero-badge">
              <Sparkles size={16} />
              AI-powered content insights
            </div>

            <h1>
              Turn your content into
              <span>
                better engagement
              </span>
            </h1>

            <p>
              Upload a PDF or image containing
              your social media content. We'll
              extract the text and analyze it
              for engagement opportunities.
            </p>

          </section>

        )}


        {error && (

          <div className="global-error">
            {error}
          </div>

        )}


        {!result && !loading && (

          <section className="upload-section">

            <FileUploader
              onAnalyze={handleAnalyze}
              loading={loading}
            />

          </section>

        )}


        {loading && (

          <LoadingSpinner />

        )}


        {result && !loading && (

          <AnalysisResult
            result={result}
            onReset={handleReset}
          />

        )}

      </main>


      <footer>

        <p>
          Social Media Content Analyzer
        </p>

        <p>
          Built for technical assessment
        </p>

      </footer>

    </div>
  );
}