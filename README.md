# subtitlesConverter
Reformat VTT, SRT subtitle. Replace words.

PowerDirector�Ŏ���(.srt)���o�͂���
Teams�̃r�f�I�Ńg�����X�N���v�g(.vtt)���o�͂���

�t�@�C���� S:\rec\�^���t�H���_�z���̃T�u�t�H���_�ɔz�u����
����afolder
����anotherfolder
�i�����j
����anotherfolder
����anotherfolder

���Ƃ���
 S:\rec\�^��\20240517_�L�b�N�I�t �̃f�B���N�g��
2024/05/21  13:43       145,596,713 rec�l�v���W�F�N�g_�L�b�N�I�t�~�[�e�B���O-20240517_103925-��c�̘^��.mp4
2024/06/17  07:00           135,734 subtitle.srt

���̌�APython�X�N���v�g�ŕҏW����
�Epython : 3�̈���ł����ϐ��ǉ�����œ���
�Epython ����� pandas���C�u�����𗘗p
�@pandas �ǉ������Fpip install pandas

�S�Ă��܂Ƃ߂ď�������o�b�`
convall.bat
��rec�t�H���_�����ɂ�����܂ރv���O������z�u���Ă���O��œ���
���t�H���_���͏�Lbat���̊��ϐ��Œ�`

���ꂼ��̃v���O�������ƂɎ��s����ꍇ

���� S:\rec> �z���ɂ���Ƃ��āF

��PowerDirector�����ɂ��Ă�

subtitle.srt ����͂Ƃ��ďo�͂�002.txt�փ��_�C���N�g
S:\rec>python printline3.py > 002.txt

002.txt ����͂Ƃ��ďo�͂�003.txt�փ��_�C���N�g
S:\rec>python removeCRLF.py > 003.txt

���g�����X�N���v�g����(vtt)�ɂ��Ă�

*.vtt ����͂Ƃ��ďo�͂�103.txt�փ��_�C���N�g
S:\rec>python printlinevtt.py > 103.txt

��AI�����̕��������Ȃǂ𖳗����C������ɂ�

?03.txt �� conv.csv ����͂Ƃ��ďo�͂� ?03-conv.txt�փ��_�C���N�g
�ϊ����ʂ͒u��������f�[�^ conv.csv ����