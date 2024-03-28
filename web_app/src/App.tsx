import "@mantine/core/styles.css";
import {
  ActionIcon,
  Box,
  Collapse,
  Group,
  MantineProvider,
  Slider,
  Space,
  Text,
} from "@mantine/core";
import { theme } from "./theme";
import { DragDrop } from "./components/DragDrop";
import { FileList } from "./components/FileList";
import { useState } from "react";
import { Button } from "@mantine/core";
import {
  IconChevronDown,
  IconChevronUp,
  IconSettingsCog,
} from "@tabler/icons-react";
import { QuestionTable } from "./components/QuestionTable";
import { v4 as uuidv4 } from "uuid";

import "./App.css";
import { API_URL } from "./env.ts";
import { useDisclosure } from "@mantine/hooks";

export interface Question {
  id: string;
  text: string;
  score: number;
}

export default function App() {
  const [files, setFiles] = useState<File[]>([]);
  const [selection, setSelection] = useState<string[]>([]);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [topK, setTopK] = useState<number>(1);
  const [distanceThreshold, setDistanceThreshold] = useState<number>(0.5);
  const [openedSettings, { toggle: toggleSettings }] = useDisclosure(false);

  const generateQuestions = async () => {
    setLoading(true);
    const formData = new FormData();
    files.forEach((file) => {
      formData.append("files", file);
    });

    formData.append("top_k", topK.toString());
    formData.append("distance_threshold", distanceThreshold.toString());

    try {
      const response = await fetch(`${API_URL}/generate_questions`, {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        const questionsWithId = data.questions.map(
          (question: { text: string; similarity_score: number }) => {
            return {
              id: uuidv4(),
              text: question.text,
              score: question.similarity_score,
            };
          },
        );
        setQuestions(questionsWithId);
      }
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <MantineProvider theme={theme}>
      <div className="body">
        <div className="upload-section">
          <DragDrop files={files} setFiles={setFiles} />

          <FileList files={files} setFiles={setFiles} />
        </div>

        <Box mt="sm">
          <Group>
            <ActionIcon onClick={toggleSettings} variant="light" color="dark">
              {openedSettings ? <IconChevronUp /> : <IconChevronDown />}
            </ActionIcon>
            <Text
              tt="uppercase"
              fw="bold"
              c="dark"
            >
              Configure model generation settings
            </Text>
          </Group>
          <Space h={8} />
          <Collapse in={openedSettings} transitionDuration={0}>
            <Text size="sm">Top K</Text>
            <Slider
              value={topK}
              onChange={setTopK}
              min={1}
              max={16}
              step={1}
              color="cyan"
            />
            <Text size="sm">Similarity Threshold</Text>
            <Slider
              value={distanceThreshold}
              onChange={setDistanceThreshold}
              min={0}
              max={1}
              step={0.1}
              color="cyan"
            />
          </Collapse>
        </Box>

        <div className="generate-section">
          <Button
            loading={loading}
            onClick={generateQuestions}
            disabled={files.length === 0 || loading}
            leftSection={<IconSettingsCog />}
            variant="gradient"
            gradient={{ from: "blue", to: "cyan", deg: 90 }}
          >
            Generate Questions
          </Button>
        </div>
        <div className="question-section">
          <QuestionTable
            selection={selection}
            setSelection={setSelection}
            questions={questions}
          />
        </div>
      </div>
    </MantineProvider>
  );
}
