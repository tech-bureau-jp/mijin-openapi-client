import { defineConfig } from "orval";

export default defineConfig({
  axiosClient: {
    input: {
      target: "../openapi3.yml",
    },
    output: {
      mode: "single",
      target: "./axios-client/src/index.ts",
      client: "axios",
    },
  },
  reactQueryClient: {
    input: {
      target: "../openapi3.yml",
    },
    output: {
      mode: "single",
      target: "./react-query-client/src/index.ts",
      client: "react-query",
    },
  },
});
