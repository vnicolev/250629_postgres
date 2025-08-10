## 確認所有虛擬環境

```bash
conda env list
```

## 建立虛擬環境

```bash
conda create --name {虛擬環境名} python={版本號}
```

## 進入特定虛擬環境

```bash
conda activate {虛擬環境名}
```

## 退出虛擬環境

```bash
conda deactivate
```

## 取消 terminal 一開始就進入 base 虛擬環境

```bash
conda config --set auto_activate_base false
```
