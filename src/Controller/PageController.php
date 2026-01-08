<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\HttpFoundation\BinaryFileResponse;
use Symfony\Component\HttpFoundation\ResponseHeaderBag;

class PageController extends AbstractController
{
    #[Route('/', name: 'app_home')]
    public function home(): Response
    {
        $reportPath = $this->getParameter('kernel.project_dir') . '/Network_Report.md';
        $reportContent = null; // Par défaut, on ne met rien

        // On ne charge le contenu que si le fichier existe ET qu'on le souhaite vraiment
        // Ici, on peut décider de ne l'afficher que si le fichier a été modifié il y a moins de 10 minutes
        // Ou simplement laisser l'utilisateur décider.
        
        if (file_exists($reportPath)) {
            $reportContent = file_get_contents($reportPath);
        }

        return $this->render('home/index.html.twig', [
            'reportContent' => $reportContent
        ]);
    }

    #[Route('/reset-analysis', name: 'reset_analysis')]
    public function reset(): Response
    {
        $projectRoot = $this->getParameter('kernel.project_dir');
        $csv = $projectRoot . '/public/Network_Analysis.csv';
        $md = $projectRoot . '/Network_Report.md';

        if (file_exists($csv)) unlink($csv);
        if (file_exists($md)) unlink($md);

        $this->addFlash('info', 'Le système a été réinitialisé. Les anciens rapports ont été supprimés.');

        return $this->redirectToRoute('app_home');
    }

    #[Route('/run-python', name: 'run_python')]
    public function runPython(): Response
    {
        $projectRoot = $this->getParameter('kernel.project_dir');
        
        // Exécution des deux scripts l'un après l'autre
        $command = "python $projectRoot/scripts/txt_to_csv.py && python $projectRoot/scripts/csv_to_md.py";
        shell_exec($command);

        $this->addFlash('success', 'Analyse terminée ! Le rapport a été mis à jour.');
        return $this->redirectToRoute('app_home');
    }

    #[Route('/portfolio', name: 'app_portfolio')]
    public function portfolio(): Response
    {
        return $this->render('portfolio/index.html.twig');
    }

    #[Route('/procedure/{_locale}', name: 'app_procedure', defaults: ['_locale' => 'fr'])]
    public function procedure(string $_locale): Response
    {
        // On définit les textes pour les deux langues
        $texts = [
            'fr' => [
                'title' => 'Guide : Analyse du Trafic Réseau',
                'phase1_title' => 'Phase 1 : Structuration des données',
                'phase1_desc' => 'Avant de commencer l\'analyse, nous devons transformer la sortie brute tcpdump en format structuré.',
                'btn_switch' => 'Switch to English',
                'target_locale' => 'en'
            ],
            'en' => [
                'title' => 'Guide : Network Traffic Analysis',
                'phase1_title' => 'Phase 1: Data Structuring',
                'phase1_desc' => 'Before starting the analysis, we must transform the raw tcpdump output into a structured format.',
                'btn_switch' => 'Passer en Français',
                'target_locale' => 'fr'
            ]
        ];

        // On récupère la version correspondante ou 'fr' par défaut
        $content = $texts[$_locale] ?? $texts['fr'];

        return $this->render('procedure/index.html.twig', [
            'content' => $content,
            'current_locale' => $_locale
        ]);
    }


    #[Route('/download-report', name: 'download_report')]
    public function downloadReport(): Response
    {
        $reportPath = $this->getParameter('kernel.project_dir') . '/Network_Report.md';

        if (!file_exists($reportPath)) {
            $this->addFlash('error', 'Le fichier n\'existe pas encore. Lancez l\'analyse d\'abord.');
            return $this->redirectToRoute('app_home');
        }

        $response = new BinaryFileResponse($reportPath);
        
        // Définit le nom du fichier lors du téléchargement
        $response->setContentDisposition(
            ResponseHeaderBag::DISPOSITION_ATTACHMENT,
            'Network_Report.md'
        );

        return $response;
    }
}