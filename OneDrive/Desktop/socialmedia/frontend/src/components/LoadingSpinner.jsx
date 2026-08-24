import { LoaderCircle } from "lucide-react";

export default function LoadingSpinner() {
  return (
    <div className="loading-container">
      <LoaderCircle
        className="spinner"
        size={40}
      />

      <p>
        Extracting and analyzing your content...
      </p>
    </div>
  );
}