# BERT/RoBERTa/DistilBERT and masked language modeling

In this example, we use dynamic masking with fine-tunes distilBERT on WikiText-2. We're using the same loss that was used during pre-training: mask language modeling. 

```sh
python run_mlm.py \
    --model_name_or_path 'distilbert-base-uncased' \
    --dataset_name wikitext \
    --dataset_config_name wikitext-2-raw-v1 \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --do_train \
    --do_eval \
    --output_dir /output/test-mlm
```
To run on your own training and validation files, use the following command
```sh
python run_mlm.py \
    --model_name_or_path roberta-base \
    --train_file path_to_train_file \
    --validation_file path_to_validation_file \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --do_train \
    --do_eval \
    --output_dir /output/test-mlm
```