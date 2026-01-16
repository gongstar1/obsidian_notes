# Speech Recognition

## Papers

### Multi-Level Embedding Conformer Framework for Bengali ASR (2026)

**Source**: [arXiv:2601.09710](https://arxiv.org/pdf/2601.09710)

**Key Contributions**:
- **Multi-level embedding fusion**: Integrates phoneme, syllable, and wordpiece embeddings
- **Conformer-CTC backbone**: Combines convolution with self-attention mechanisms
- **Low-resource language focus**: Addresses Bengali ASR challenges (morphologically rich, 300M+ speakers)

**Architecture**:
```
Audio → Preprocessing → Early Conformer → Multi-level Embedding Fusion → Late Conformer → CTC Decoder → Text
                                    ↓
                    ┌───────────────┼───────────────┐
                Phoneme       Syllable      Wordpiece
                Embedding      Embedding     Embedding
```

**Technical Details**:
- **Dataset**: OpenSLR Large Bengali ASR (196k utterances, 181.5 hours, 204k FLAC files)
- **Preprocessing**: Silence trimming, resampling, Log-Mel spectrogram, SpecAugment
- **Model**: 36 Conformer blocks (early + late stages)
- **Training**: 100 epochs, batch size 32, Adam optimizer, learning rate 1e-4

**Performance**:
- **WER**: 10.01% (word-level accuracy)
- **CER**: 5.03% (character-level accuracy)
- Outperforms previous approaches (LSTM-RNN: 28.70% WER, GRU: 54.19% WER)

**Key Innovations**:
1. Multi-granularity linguistic representation (phoneme + syllable + wordpiece)
2. Parallel embedding networks capture complementary linguistic information
3. Fusion mechanism: `H(F) = H(E) + E_phoneme + E_syllable + E_wordpiece`
4. Scalable to other low-resource languages

**Comparison with SOTA**:
| Method | WER (%) | CER (%) | Dataset |
|--------|---------|---------|---------|
| GRU | 54.19 | - | OpenSLR |
| LSTM-RNN | 28.70 | 13.20 | OpenSLR |
| Wav2Vec2 | 25.24 | - | Common Voice |
| **Proposed** | **10.01** | **5.03** | OpenSLR |

---

## Trends
#Speech synthsis
